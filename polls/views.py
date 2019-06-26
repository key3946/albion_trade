import datetime
import os
import re
import shutil
import json
from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
import git
import logging

from polls.models import Good

logger = logging.getLogger(__name__)
IS_RENEW_CONTINUE = False
LAST_RENEW_TIME = datetime.datetime.__init__(datetime, 2000, 1, 1, 0, 0, 0, 0,)
print(LAST_RENEW_TIME)


def index(request):
    context = {
        'title': 'Albion Trader - Make your big money'
    }
    return render(request, 'polls/index.html', context)


def contact(request):
    context = {
        'title': _('Albion Trader - Contact'),
        'hero_title': _('Contact'),
        'hero_subtitle': _('Don\'t kill me (ToT)')
    }
    return render(request, 'polls/contact.html', context)


def rank(request):
    context = {
        'title': _('Albion Trader - Analyze')
    }
    return render(request, 'polls/rank.html', context)


def about(request):
    context = {
        'title': _('Albion Trader - About'),
        'hero_title': _('About'),
        'hero_subtitle': _('Head to happiness')
    }
    return render(request, 'polls/about.html', context)


def license_(request):
    context = {
        'title': _('Albion Trader - License'),
        'hero_title': _('License'),
        'hero_subtitle': _('I agree and respect the following')
    }
    return render(request, 'polls/license.html', context)


def renew(request):
    return


def check_between_local_remote_git(dump_path):
    def lsremote(url):
        remote_refs = {}
        g = git.cmd.Git()
        for ref in g.ls_remote(url).split('\n'):
            hash_ref_list = ref.split('\t')
            remote_refs[hash_ref_list[1]] = hash_ref_list[0]
        return remote_refs

    refs = lsremote('https://github.com/broderickhyman/ao-bin-dumps.git')
    remote_hexsha = refs["HEAD"]
    repo = git.Repo(dump_path)
    local_hexsha = repo.iter_commits("HEAD").__next__().hexsha
    return remote_hexsha == local_hexsha


def clone_dumps(dump_path):
    # 最新アイテムリストを取得
    def recursive_file_check(path):
        if os.path.isdir(path):
            # directoryだったら中のファイルに対して再帰的にこの関数を実行
            files = os.listdir(path)
            for file in files:
                recursive_file_check(path + "\\" + file)
        else:
            # fileだったら処理
            os.chmod(path, 0o777)
            os.remove(path)

    recursive_file_check(dump_path)
    if os.path.exists(dump_path):
        shutil.rmtree(dump_path)
    git.Repo.clone_from('https://github.com/broderickhyman/ao-bin-dumps.git', dump_path, branch='master')


def create_good_object_from_dump(dump_path):
    # dumpsの中のアイテムをModelに変換
    with open(dump_path + '/formatted/items.json', 'r', encoding="utf-8") as json_file:
        items = json.load(json_file)

    # jsonのキーをすべてsnake caseにする(関数)

    def camel_to_underscore(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def convert_json(d, convert):
        new_d = {}
        for k, v in d.items():
            new_d[convert(k)] = convert_json(v, convert) if isinstance(v, dict) else v
        return new_d

    goods_for_db = []
    for item in items:
        # jsonのキーをすべてsnake caseにする(実行)
        item = convert_json(item, camel_to_underscore)
        if not Good.objects.filter(unique_name=item["unique_name"]).exists():

            good = Good(
                localization_name_variable=item["localization_name_variable"],
                localization_description_variable=item["localization_description_variable"],
                index=item["index"],
                unique_name=item["unique_name"],
            )
            goods_for_db.append(good)
        else:
            continue
    Good.objects.bulk_create(goods_for_db)


def renew_all(request):
    global IS_RENEW_CONTINUE
    if not IS_RENEW_CONTINUE:
        IS_RENEW_CONTINUE = True
        logger.info("Renew Goods Start")
        dump_path = 'polls/dumps'
        if not check_between_local_remote_git(dump_path):
            clone_dumps(dump_path)
        create_good_object_from_dump(dump_path)
        IS_RENEW_CONTINUE = False
        logger.info("Renew Goods End")
    else:
        logger.info("Renew Goods still continue")

    return render(request, "polls/index.html", context={})


def price(request):
    return


def profit_all(request):
    return


def profit_item(request):
    return
