<a href='https://github.com/Junwu0615/Platform Genesis'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Platform Genesis.svg'>
[![Back to HomePage](https://img.shields.io/badge/%F0%9F%8C%90_Back_to-HomePage-blue?style=flat-square)](https://github.com/Junwu0615/Platform-Genesis)

## *⭐ Platform Genesis Universe Analytics ⭐*
> _🧟‍♂️ Initial startup time data ( March – June 2026 ) was not_ 
> _captured due to the absence of a record-keeping script._
<!-- update_time:start -->
>
> _Generated at [ UTC+0 ] :　2026-07-08T17:50:36_

<!-- update_time:end -->

<br>

### *📌　Implement*

<details>
<summary><b><i>　Tree </i></b></summary>
<ul>

```bash
tree -I 'venv|.git|__pycache__|docs|logs|assets|kafka_data|charts'

.
├── LICENSE
├── README.md
├── config
│   ├── analytics.yml
│   └── repositories.yml
├── data
│   ├── latest
│   │   ├── PG-APP-Core.json
│   │   ├── PG-Airflow-DAGs.json
│   │   ├── PG-Analytics.json
│   │   ├── PG-Core.json
│   │   ├── PG-Cortex.json
│   │   ├── PG-Edge-Container.json
│   │   ├── PG-Infrastructure.json
│   │   ├── PG-Sentinel.json
│   │   ├── PG-Shared-Lib.json
│   │   ├── PG-Synapse.json
│   │   └── Platform-Genesis.json
│   └── summary.json
├── history
│   ├── 2026-07.csv
│   ├── ....
│   └── 20xx-xx.csv
├── reports
│   ├── dashboard.md
│   ├── growth.md
│   ├── summary.md
│   ├── traffic.md
│   └── update_time.md
├── requirements.txt
└── scripts
    ├── collect.py
    ├── export_history.py
    ├── generate_report.py
    ├── sync_readme.py
    └── utils.py

```

</ul>
</details>

<details>
<summary><b><i>　Workflow </i></b></summary>
<ul>

```bash
# STAGE. 1
 • collect.py
      ↓
 • data/latest/*.json
   ( 最新快照 )


# STAGE. 2
 • export_history.py
      ↓
 • history/YYYY-MM-history.csv
   ( 每日快照累積 / 按月分區 )


# STAGE. 3
 • generate_report.py
      ↓
 • data/summary.json
   ( 所有 Repo 最新統計總覽 )
      ↓
 • dashboard.md ( 目前快照 )
 • traffic.md   ( 近 14 天流量 )
 • growth.md    ( 本月累積成長 )
 • summary.md   ( 總覽報表 )

# STAGE. 4
 • sync_readme.py
      ↓
 • README.md
   ( 所有 Report 渲染至首頁 )
```

</ul>
</details>

<br>

### *📋　Repository Summary Report*

<!-- summary:start -->
> _Note :　Metrics are aggregated across all tracked repositories._

| *📐 Metric* | *🧮 Value* |
|:--|--:|
| *📁 Total Repositories* | *11* |
| *⭐ Total Stars* | *12* |
| *🍴 Total Forks* | *0* |
| *📦 Size (MB)* | *55.27* |
| *👀 Total Views* | *948* |
| *👤 Total Unique Visitors* | *39* |
| *📥 Total Clones* | *2186* |
| *👤 Total Unique Cloners* | *847* |
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->

 | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *📦 Size (MB)* | *📝 Last Updated* | *📅 Creation Date* |
 |:--|--:|--:|--:|--:|--:|
 | *Platform-Genesis* | *2* | *0* | *47.64* | *2026-07-07* | *2026-03-20* |
 | *PG-Core* | *1* | *0* | *2.05* | *2026-07-06* | *2026-07-03* |
 | *PG-Synapse* | *1* | *0* | *0.00* | *2026-07-05* | *2026-07-03* |
 | *PG-Cortex* | *1* | *0* | *0.01* | *2026-07-05* | *2026-07-03* |
 | *PG-Sentinel* | *1* | *0* | *0.00* | *2026-07-05* | *2026-07-03* |
 | *PG-Analytics* | *1* | *0* | *0.18* | *2026-07-07* | *2026-07-03* |
 | *PG-Infrastructure* | *1* | *0* | *5.10* | *2026-07-07* | *2026-05-08* |
 | *PG-APP-Core* | *1* | *0* | *0.15* | *2026-07-08* | *2026-05-08* |
 | *PG-Shared-Lib* | *1* | *0* | *0.05* | *2026-06-22* | *2026-05-08* |
 | *PG-Edge-Container* | *1* | *0* | *0.03* | *2026-06-22* | *2026-05-08* |
 | *PG-Airflow-DAGs* | *1* | *0* | *0.06* | *2026-06-22* | *2026-05-08* |
<!-- dashboard:end -->

<br>

### *🔍　Traffic Analytics*

<!-- traffic:start -->
> _Traffic in the past **14 Days**_

| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |
|:--|--:|--:|--:|--:|
| *Platform-Genesis* | *319* | *16* | *554* | *209* |
| *PG-Core* | *80* | *2* | *295* | *121* |
| *PG-Synapse* | *26* | *3* | *48* | *31* |
| *PG-Cortex* | *30* | *2* | *41* | *26* |
| *PG-Sentinel* | *24* | *2* | *32* | *25* |
| *PG-Analytics* | *343* | *3* | *968* | *314* |
| *PG-Infrastructure* | *71* | *3* | *174* | *74* |
| *PG-APP-Core* | *20* | *2* | *55* | *31* |
| *PG-Shared-Lib* | *14* | *2* | *10* | *7* |
| *PG-Edge-Container* | *9* | *1* | *4* | *4* |
| *PG-Airflow-DAGs* | *12* | *3* | *5* | *5* |
- ### *Summary*
  - *👀 Views :　948*
  - *👤 Unique Visitors :　39*
  - *📥 Clones :　2186*
  - *👤 Unique Cloners :　847*
<!-- traffic:end -->

<br>

### *📈　Monthly Growth Analytics*

<!-- growth:start -->
> _Statistical Scope :　**2026-07**_

| *📁 Repository* | *⭐ Stars ↕* | *🍴 Forks ↕* | *💡 Open Issues ↕* | *👀 Views ↕<br>( 14 Days )* | *📥 Clones ↕<br>( 14 Days )* |
|:--|--:|--:|--:|--:|--:|
| *Platform-Genesis* | *+0* | *+0* | *+0* |*+47* | *-247* | 
| *PG-Core* | *+0* | *+0* | *+0* |*+82* | *+416* | 
| *PG-Synapse* | *+0* | *+0* | *+0* |*+29* | *+79* | 
| *PG-Cortex* | *+0* | *+0* | *+0* |*+32* | *+67* | 
| *PG-Sentinel* | *+0* | *+0* | *+0* |*+26* | *+57* | 
| *PG-Analytics* | *+0* | *+0* | *+0* |*+346* | *+1282* | 
| *PG-Infrastructure* | *+0* | *+0* | *+0* |*-41* | *-609* | 
| *PG-APP-Core* | *+0* | *+0* | *+0* |*+7* | *-60* | 
| *PG-Shared-Lib* | *+0* | *+0* | *+0* |*+8* | *-33* | 
| *PG-Edge-Container* | *+0* | *+0* | *+0* |*+4* | *-79* | 
| *PG-Airflow-DAGs* | *+0* | *+0* | *+0* |*+4* | *-33* | 
<!-- growth:end -->


<br><br><br>