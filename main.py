import requests
import re

# Список URL для поиска
urls = ['https://console.3.s3.itmo.ru', 'https://www.events.itmo.ru', 'https://personal-path.du.itmo.ru', 'https://www.aitalents.itmo.ru', 'https://www.konkurs.future.itmo.ru', 'https://hosting6.it.itmo.ru', 'https://online-start.itmo.ru', 'https://wifi-dici.itmo.ru', 'https://www.kronbars.itmo.ru', 'https://nifi.demo.it.itmo.ru', 'https://military.itmo.ru', 'https://mentalhealth.itmo.ru', 'https://schoolpi.itmo.ru', 'https://www.lr.news.itmo.ru', 'https://www.competition.future.itmo.ru', 'https://www.cdpo.itmo.ru', 'https://ad.physics.itmo.ru', 'https://mirror.dis.itmo.ru', 'https://doc.physics.itmo.ru', 'https://aicidlab.itmo.ru', 'https://dc.itmo.ru', 'https://www.mentalhealth.itmo.ru', 'https://fizmat.itmo.ru', 'https://api.future.itmo.ru', 'https://icpc.itmo.ru', 'https://forumonline.itmo.ru', 'https://uxr.itmo.ru', 'https://fnte.itmo.ru', 'https://ch.itmo.ru', 'https://www.greentech.itmo.ru', 'https://www.chgk.itmo.ru', 'https://api.it.itmo.ru', 'https://school.physics.itmo.ru', 'https://www.be.itmo.ru', 'https://www.publichealth.itmo.ru', 'https://www.dk.itmo.ru', 'https://centrsio.itmo.ru', 'https://hq.itmo.ru', 'https://api.demo2.hq.itmo.ru', 'https://hosting4.it.itmo.ru', 'https://www.ftmi.itmo.ru', 'https://qpmlab.itmo.ru', 'https://hosting3.it.itmo.ru', 'https://program-adviser.du.itmo.ru', 'https://activity-navigator.du.itmo.ru', 'https://www.programming.itmo.ru', 'https://www.art.online.itmo.ru', 'https://wiki.itmo.ru', 'https://metanano.itmo.ru', 'https://rektorkrut.itmo.ru', 'https://t-masters.itmo.ru', 'https://sai.itmo.ru', 'https://api.parks.urban.itmo.ru', 'https://en.itmo.ru', 'https://camp.itmo.ru', 'https://www.team.itmo.ru', 'https://scicomm.itmo.ru', 'https://demo2.hq.itmo.ru', 'https://niu.itmo.ru', 'https://graphicon.itmo.ru', 'https://rft21.itmo.ru', 'https://konkurs.future.itmo.ru', 'https://job.itmo.ru', 'https://stock.itmo.ru', 'https://nas.it.itmo.ru', 'https://mgmt.itmo.ru', 'https://art.itmo.ru', 'https://open-education.du.itmo.ru', 'https://bbb.v.itmo.ru', 'https://parks.urban.itmo.ru', 'https://openeducation.itmo.ru', 'https://physics.itmo.ru', 'https://mega.itmo.ru', 'https://old-abit.itmo.ru', 'https://moodleftmi.itmo.ru', 'https://demo.hub.itmo.ru', 'https://redmine.physics.itmo.ru', 'https://www.ipkn.itmo.ru', 'https://l1.lis.itmo.ru', 'https://www.schoolpi.itmo.ru', 'https://latex.physics.itmo.ru', 'https://ktuschool.itmo.ru', 'https://digest.itmo.ru', 'https://night.technopark.itmo.ru', 'https://www.automata.itmo.ru', 'https://lib.itmo.ru', 'https://publichealth.itmo.ru', 'https://admin.itmo.ru', 'https://slalom.physics.itmo.ru', 'https://chgk.itmo.ru', 'https://alccloud.v.itmo.ru', 'https://media.itmo.ru', 'https://signup.itmo.ru', 'https://fict.itmo.ru', 'https://serv1.aicidlab.itmo.ru', 'https://clab.itmo.ru', 'https://museum.itmo.ru', 'https://aip.itmo.ru', 'https://bonustrack.itmo.ru', 'https://teams.secure.itmo.ru', 'https://www.itmo.ru', 'https://urban.itmo.ru', 'https://ipkn.itmo.ru', 'https://chat.physics.itmo.ru', 'https://warehouse.it.itmo.ru', 'https://ik.proxy.itmo.ru', 'https://energylab.itmo.ru', 'https://vdi2.itmo.ru', 'https://blocked.itmo.ru', 'https://online-class.du.itmo.ru', 'https://exam.ipkn.itmo.ru', 'https://softskills.itmo.ru', 'https://forms.du.itmo.ru', 'https://mhs.itmo.ru', 'https://fablab.itmo.ru', 'https://storage.itmo.ru', 'https://tt.itmo.ru', 'https://activity-path.du.itmo.ru', 'https://dms.du.itmo.ru', 'https://cs.itmo.ru', 'https://www.edpractices.itmo.ru', 'https://cccp.itmo.ru', 'https://sarsmutant.itmo.ru', 'https://neironecdot.itmo.ru', 'https://bpm.itmo.ru', 'https://docker.physics.itmo.ru', 'https://nwq.itmo.ru', 'https://megaphystech.itmo.ru', 'https://nanoworkshop.physics.itmo.ru', 'https://api.track.itmo.ru', 'https://vminsert.services.itmo.ru', 'https://itmo.ru', 'https://grf.svc.itmo.ru', 'https://ecinn.itmo.ru', 'https://microwave.school.physics.itmo.ru', 'https://aparts.itmo.ru', 'https://id.su.ya.dc.itmo.ru', 'https://helpdesk.physics.itmo.ru', 'https://bioprint.itmo.ru', 'https://publicid.itmo.ru', 'https://ec.itmo.ru', 'https://akson.itmo.ru', 'https://api.sarsmutant.itmo.ru', 'https://cloud.itmo.ru', 'https://www.clubs.itmo.ru', 'https://auth.it.itmo.ru', 'https://www.alumni.itmo.ru', 'https://5100.itmo.ru', 'https://competition.future.itmo.ru', 'https://id.hq.itmo.ru', 'https://smeshno.itmo.ru', 'https://python.physics.itmo.ru', 'https://flamn.itmo.ru', 'https://es.itmo.ru', 'https://gitlab-ct.itmo.ru', 'https://advent.itmo.ru', 'https://irs2022.itmo.ru', 'https://track.itmo.ru', 'https://foodbiotech.itmo.ru', 'https://www.start.itmo.ru', 'https://dis.itmo.ru', 'https://monitoring.dis.itmo.ru', 'https://neerc.itmo.ru', 'https://iwd.itmo.ru', 'https://gamedev.itmo.ru', 'https://edu.fablab.itmo.ru', 'https://media.ec.itmo.ru', 'https://olymp.physics.itmo.ru', 'https://scs.itmo.ru', 'https://distant.itmo.ru', 'https://tech-support.du.itmo.ru', 'https://studio.dc-edu.itmo.ru', 'https://dpht.itmo.ru', 'https://life.itmo.ru', 'https://cs-accel.itmo.ru', 'https://cn.itmo.ru', 'https://mentor-navigator.du.itmo.ru', 'https://butikov.itmo.ru', 'https://www.tefl.itmo.ru', 'https://els2021.physics.itmo.ru', 'https://docs.services.itmo.ru', 'https://www.lib.itmo.ru', 'https://www.dc.itmo.ru', 'https://sd.itmo.ru', 'https://alcdoc.v.itmo.ru', 'https://local.auth.it.itmo.ru', 'https://lr.news.itmo.ru', 'https://individual-plan.du.itmo.ru', 'https://edu-attestation.du.itmo.ru', 'https://logs.dis.itmo.ru', 'https://prod.auth.it.itmo.ru', 'https://personal-schedule.du.itmo.ru', 'https://id.itmo.ru', 'https://innovation.itmo.ru', 'https://www.energylab.itmo.ru', 'https://bars.itmo.ru', 'https://greentech.itmo.ru', 'https://cdpo.itmo.ru', 'https://www.monitor.dc.it.itmo.ru', 'https://slalom.itmo.ru', 'https://ichem.itmo.ru', 'https://az.proxy.itmo.ru', 'https://webhosting.itmo.ru', 'https://careers.itmo.ru', 'https://apart.itmo.ru', 'https://www.pish.itmo.ru', 'https://opendoors.itmo.ru', 'https://www.opendoors.itmo.ru', 'https://dns.it.itmo.ru', 'https://virt-hvs03t.physics.itmo.ru', 'https://project.cps.it.itmo.ru', 'https://recycle.itmo.ru', 'https://alumni.itmo.ru', 'https://sm.itmo.ru', 'https://testmoodle.itmo.ru', 'https://l4.lis.itmo.ru', 'https://edpractices.itmo.ru', 'https://virt-hvs04p.physics.itmo.ru', 'https://microservices.itmo.ru', 'https://www.ecinn.itmo.ru', 'https://news.egov.itmo.ru', 'https://voting.itmo.ru', 'https://kronbars.itmo.ru', 'https://els-2020.itmo.ru', 'https://study.physics.itmo.ru', 'https://els-spb.physics.itmo.ru', 'https://survey.itmo.ru', 'https://fspo.itmo.ru', 'https://family.itmo.ru', 'https://pcms.itmo.ru', 'https://gar.itmo.ru', 'https://lc.fablab.itmo.ru', 'https://crm.itmo.ru', 'https://optimus.itmo.ru', 'https://news.itmo.ru', 'https://student.itmo.ru', 'https://www.pi.itmo.ru', 'https://dk.itmo.ru', 'https://technopark.itmo.ru', 'https://openbooks.itmo.ru', 'https://www.aparts.itmo.ru', 'https://cloverschool.itmo.ru', 'https://automata.itmo.ru', 'https://holoschool.itmo.ru', 'https://stars.itmo.ru', 'https://be.itmo.ru', 'https://www.future.itmo.ru', 'https://itcenter.itmo.ru', 'https://infdiscussion.itmo.ru', 'https://wiki.physics.itmo.ru', 'https://www.wish.itmo.ru', 'https://itmoleaders.itmo.ru', 'https://olymp2.itmo.ru', 'https://opensciencefest.itmo.ru', 'https://isu.itmo.ru', 'https://edu.itmo.ru', 'https://phone.api.it.itmo.ru', 'https://abitlk.itmo.ru', 'https://stopcovid.itmo.ru', 'https://studnauka.itmo.ru', 'https://www.love.itmo.ru', 'https://event.itmo.ru', 'https://int.itmo.ru', 'https://oecs.physics.itmo.ru', 'https://connect.itmo.ru', 'https://kmu.itmo.ru', 'https://agni.itmo.ru', 'https://hp.itmo.ru', 'https://start.itmo.ru', 'https://www.scicomm.itmo.ru', 'https://cdn.itmo.ru', 'https://accel.itmo.ru', 'https://team.itmo.ru', 'https://zabbix.physics.itmo.ru', 'https://cifru-meet.itmo.ru', 'https://monitor.dc.it.itmo.ru', 'https://personal-growth.du.itmo.ru', 'https://l2.lis.itmo.ru', 'https://research.itmo.ru', 'https://welcomespb.itmo.ru', 'https://it.itmo.ru', 'https://virt-hvs02t.physics.itmo.ru', 'https://ns.itmo.ru', 'https://dev.api.isu.itmo.ru', 'https://www.abit.itmo.ru', 'https://helpdesk.itmo.ru', 'https://www.ichem.itmo.ru', 'https://expert.itmo.ru', 'https://mse.itmo.ru', 'https://mcp.itmo.ru', 'https://www.leader.itmo.ru', 'https://api.demo1.hq.itmo.ru', 'https://diploma.itmo.ru', 'https://wireless.school.physics.itmo.ru', 'https://git.physics.itmo.ru', 'https://www.ai.itmo.ru', 'https://holo.itmo.ru', 'https://leader.itmo.ru', 'https://www.iwd.itmo.ru', 'https://dev.auth.it.itmo.ru', 'https://course-development.du.itmo.ru', 'https://www.art.itmo.ru', 'https://apps.dc-edu.itmo.ru', 'https://lifesafety.itmo.ru', 'https://new.itmo.ru', 'https://www.vc.itmo.ru', 'https://dc-edu.itmo.ru', 'https://www.diploma.itmo.ru', 'https://wud.itmo.ru', 'https://clubs.itmo.ru', 'https://ct.itmo.ru', 'https://www.stars.itmo.ru', 'https://preview.dc-edu.itmo.ru', 'https://www.survey.itmo.ru', 'https://courses.sf.itmo.ru', 'https://2030.itmo.ru', 'https://solgel2019.itmo.ru', 'https://checkin.itmo.ru', 'https://www.ct.itmo.ru', 'https://health.itmo.ru', 'https://kids.itmo.ru', 'https://online-pk.itmo.ru', 'https://courses.du.itmo.ru', 'https://edu.kids.itmo.ru', 'https://vault.services.itmo.ru', 'https://1.s3.itmo.ru', 'https://coding.itmo.ru', 'https://www.bonustrack.itmo.ru', 'https://cloud.physics.itmo.ru', 'https://events.itmo.ru', 'https://biosensing.school.physics.itmo.ru', 'https://www.digest.itmo.ru', 'https://idu.itmo.ru', 'https://aitalents.itmo.ru', 'https://neuronecdote.itmo.ru', 'https://spot.itmo.ru', 'https://catalog.physics.itmo.ru', 'https://online.itmo.ru', 'https://studio.du.itmo.ru', 'https://b2b.itmo.ru', 'https://www.mega.itmo.ru', 'https://m.online.itmo.ru', 'https://www.urban.itmo.ru', 'https://pish.itmo.ru', 'https://op.itmo.ru', 'https://logs.physics.itmo.ru', 'https://deep-learning.itmo.ru', 'https://sciencerunner.itmo.ru', 'https://my.itmo.ru', 'https://www.accel.itmo.ru', 'https://email.itmo.ru', 'https://cit.itmo.ru', 'https://www.mhs.itmo.ru', 'https://qrwork.itmo.ru', 'https://utils.physics.itmo.ru', 'https://sf.itmo.ru', 'https://pi.itmo.ru', 'https://verification.du.itmo.ru', 'https://www.deep-learning.itmo.ru', 'https://schools.itmo.ru', 'https://vc.itmo.ru', 'https://art.online.itmo.ru', 'https://yagodnoe.itmo.ru', 'https://itm.itmo.ru', 'https://adts.itmo.ru', 'https://www.expert.itmo.ru', 'https://egose.itmo.ru', 'https://edu-management.du.itmo.ru', 'https://aicltr.itmo.ru', 'https://aspirantura.itmo.ru', 'https://olymp.itmo.ru', 'https://rchat.itmo.ru', 'https://dx.itmo.ru', 'https://www.health.itmo.ru', 'https://120.itmo.ru', 'https://games.kronbars.itmo.ru', 'https://parsec-dev.it.itmo.ru', 'https://fellowship.itmo.ru', 'https://mrischool.physics.itmo.ru', 'https://www.apart.itmo.ru', 'https://lfo.itmo.ru', 'https://fitp.itmo.ru', 'https://tgbot.it.itmo.ru', 'https://abit.itmo.ru', 'https://learn.physics.itmo.ru', 'https://www.welcomespb.itmo.ru', 'https://lifeinscience.itmo.ru', 'https://fpo.itmo.ru', 'https://future.itmo.ru', 'https://hyperjump.itmo.ru', 'https://esp.itmo.ru', 'https://ckp-nt.physics.itmo.ru', 'https://moodle.itmo.ru', 'https://ftmi.itmo.ru', 'https://www.openeducation.itmo.ru', 'https://stsmasters.itmo.ru', 'https://olymp.mega.itmo.ru', 'https://www.online.itmo.ru', 'https://design.itmo.ru', 'https://yc.itmo.ru', 'https://srv.library.itmo.ru', 'https://next.itmo.ru', 'https://login.itmo.ru', 'https://fltc.itmo.ru', 'https://ip.physics.itmo.ru', 'https://lis.itmo.ru', 'https://qr.itmo.ru', 'https://programming.itmo.ru', 'https://monitoring.it.itmo.ru', 'https://log.api.it.itmo.ru', 'https://openscience.itmo.ru', 'https://radius.it.itmo.ru', 'https://www.family.itmo.ru', 'https://nerc.itmo.ru', 'https://ai.itmo.ru', 'https://pk.itmo.ru', 'https://tefl.itmo.ru', 'https://course-demand.du.itmo.ru']


# Регулярное выражение для поиска
regex_pattern = r'itmo\{(\w+)\}'

# Пустой список для хранения найденных соответствий
matches = []

# Пройдемся по каждому URL
for url in urls:
    try:
        # Отправляем GET-запрос на сайт
        response = requests.get(url)

        # Проверяем, был ли успешный ответ от сервера (код 200)
        if response.status_code == 200:
            # Используем регулярное выражение для поиска
            found = re.findall(regex_pattern, response.text)

            # Добавляем найденные соответствия в список matches
            matches.extend(found)
        else:
            print(f"Не удалось получить доступ к странице {url}. Код состояния: {response.status_code}")

    except Exception as e:
        print(f"Произошла ошибка при обращении к странице {url}: {e}")

# Выводим найденные соответствия
for match in matches:
    print(match)
