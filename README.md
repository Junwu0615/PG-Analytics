<a href='https://github.com/Junwu0615/Platform Genesis'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Platform Genesis.svg'>
[![Back to HomePage](https://img.shields.io/badge/%F0%9F%8C%90_Back_to-HomePage-blue?style=flat-square)](https://github.com/Junwu0615/Platform-Genesis)

## *⭐ Platform Genesis Universe Analytics ⭐*
> _🧟‍♂️ Initial startup time data ( March – June 2026 ) was not_ 
> _captured due to the absence of a record-keeping script._
<!-- update_time:start -->
>
> _Generated at [ UTC+0 ] :　2026-07-12T17:13:36_

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
| *📦 Size (MB)* | *57.26* |
| *👀 Total Views* | *951* |
| *👤 Total Unique Visitors* | *35* |
| *📥 Total Clones* | *2163* |
| *👤 Total Unique Cloners* | *851* |
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->

 | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *📦 Size (MB)* | *📝 Last Updated* | *📅 Creation Date* |
 |:--|--:|--:|--:|--:|--:|
 | *Platform-Genesis* | *2* | *0* | *48.88* | *2026-07-12* | *2026-03-20* |
 | *PG-Core* | *1* | *0* | *2.82* | *2026-07-12* | *2026-07-03* |
 | *PG-Synapse* | *1* | *0* | *0.00* | *2026-07-05* | *2026-07-03* |
 | *PG-Cortex* | *1* | *0* | *0.01* | *2026-07-05* | *2026-07-03* |
 | *PG-Sentinel* | *1* | *0* | *0.00* | *2026-07-05* | *2026-07-03* |
 | *PG-Analytics* | *1* | *0* | *0.20* | *2026-07-11* | *2026-07-03* |
 | *PG-Infrastructure* | *1* | *0* | *5.11* | *2026-07-10* | *2026-05-08* |
 | *PG-APP-Core* | *1* | *0* | *0.10* | *2026-07-12* | *2026-05-08* |
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
| *Platform-Genesis* | *310* | *10* | *461* | *185* |
| *PG-Core* | *86* | *3* | *305* | *125* |
| *PG-Synapse* | *26* | *3* | *50* | *33* |
| *PG-Cortex* | *30* | *2* | *43* | *28* |
| *PG-Sentinel* | *24* | *2* | *35* | *28* |
| *PG-Analytics* | *344* | *3* | *991* | *321* |
| *PG-Infrastructure* | *73* | *3* | *182* | *76* |
| *PG-APP-Core* | *21* | *2* | *83* | *45* |
| *PG-Shared-Lib* | *15* | *3* | *6* | *3* |
| *PG-Edge-Container* | *9* | *1* | *2* | *2* |
| *PG-Airflow-DAGs* | *13* | *3* | *5* | *5* |
- ### *Summary*
  - *👀 Views :　951*
  - *👤 Unique Visitors :　35*
  - *📥 Clones :　2163*
  - *👤 Unique Cloners :　851*
<!-- traffic:end -->

<br>

### *📈　Monthly Growth Analytics*

<!-- growth:start -->
> _Statistical Scope :　**2026-07**_

| *📁 Repository* | *⭐ Stars ↕* | *🍴 Forks ↕* | *💡 Open Issues ↕* | *👀 Views ↕<br>( 14 Days )* | *📥 Clones ↕<br>( 14 Days )* |
|:--|--:|--:|--:|--:|--:|
| *Platform-Genesis* | *+0* | *+0* | *+0* |*+32* | *-364* | 
| *PG-Core* | *+0* | *+0* | *+0* |*+89* | *+430* | 
| *PG-Synapse* | *+0* | *+0* | *+0* |*+29* | *+83* | 
| *PG-Cortex* | *+0* | *+0* | *+0* |*+32* | *+71* | 
| *PG-Sentinel* | *+0* | *+0* | *+0* |*+26* | *+63* | 
| *PG-Analytics* | *+0* | *+0* | *+0* |*+347* | *+1312* | 
| *PG-Infrastructure* | *+0* | *+0* | *+0* |*-39* | *-599* | 
| *PG-APP-Core* | *+0* | *+0* | *+0* |*+8* | *-18* | 
| *PG-Shared-Lib* | *+0* | *+0* | *+0* |*+10* | *-41* | 
| *PG-Edge-Container* | *+0* | *+0* | *+0* |*+4* | *-83* | 
| *PG-Airflow-DAGs* | *+0* | *+0* | *+0* |*+5* | *-33* | 
<!-- growth:end -->


<br><br><br>