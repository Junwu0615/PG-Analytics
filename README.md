<a href='https://github.com/Junwu0615/Platform Genesis'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Platform Genesis.svg'>
[![Back to HomePage](https://img.shields.io/badge/%F0%9F%8C%90_Back_to-HomePage-blue?style=flat-square)](https://github.com/Junwu0615/Platform-Genesis)

## *⭐ Platform Genesis Universe Analytics ⭐*
> _🧟‍♂️ Initial startup time data ( March – June 2026 ) was not_ 
> _captured due to the absence of a record-keeping script._

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
│   └── traffic.md
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
 • traffic.md ( 近 14 天流量 )
 • growth.md ( 本月累積成長 )
 • summary.md ( 總覽報表 )

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
>
> _Generated at [ UTC+0 ] :　2026-07-05T17:31:17_

| *📐 Metric* | *🧮 Value* |
|:--|--:|
| *📁 Total Repositories* | *11* |
| *⭐ Total Stars* | *12* |
| *🍴 Total Forks* | *0* |
| *👀 Total Views* | *940* |
| *👤 Unique Visitors* | *43* |
| *📥 Total Clones* | *2283* |
| *👤 Unique Cloners* | *851* |
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->
> _Generated at [ UTC+0 ] :　2026-07-05T17:31:17_

 | *📁<br>Repository* | *⭐<br>Stars* | *🍴<br>Forks* | *👀<br>Views* | *👤<br>Unique Visitors* | *📥<br>Clones* | *👤<br>Unique Cloners* |
 |:--|--:|--:|--:|--:|--:|--:|
 | *Platform-Genesis* | *2* | *0* | *368* | *20* | *806* | *300* |
 | *PG-Core* | *1* | *0* | *42* | *1* | *139* | *62* |
 | *PG-Synapse* | *1* | *0* | *18* | *2* | *32* | *20* |
 | *PG-Cortex* | *1* | *0* | *25* | *2* | *28* | *18* |
 | *PG-Sentinel* | *1* | *0* | *19* | *2* | *25* | *19* |
 | *PG-Analytics* | *1* | *0* | *325* | *2* | *880* | *284* |
 | *PG-Infrastructure* | *1* | *0* | *69* | *4* | *195* | *86* |
 | *PG-APP-Core* | *1* | *0* | *26* | *3* | *89* | *15* |
 | *PG-Shared-Lib* | *1* | *0* | *19* | *3* | *29* | *16* |
 | *PG-Edge-Container* | *1* | *0* | *13* | *1* | *48* | *22* |
 | *PG-Airflow-DAGs* | *1* | *0* | *16* | *3* | *12* | *9* |
- ### *Summary*
  - *📁 Repository :　11*
  - *⭐ Stars :　12*
  - *🍴 Forks :　0*
  - *👀 Views ( 14 days ) :　940*
  - *👤 Unique Visitors ( 14 days ) :　43*
  - *📥 Clones ( 14 days ) :　2283*
  - *👤 Unique Cloners ( 14 days ) :　851*
<!-- dashboard:end -->

<br>

### *🔍　Traffic Analytics*

<!-- traffic:start -->
> _Traffic in the past 14 days_
>
> _Generated at [ UTC+0 ] :　2026-07-05T17:31:17_

| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |
|:--|--:|--:|--:|--:|
| *Platform-Genesis* | *368* | *20* | *806* | *300* |
| *PG-Core* | *42* | *1* | *139* | *62* |
| *PG-Synapse* | *18* | *2* | *32* | *20* |
| *PG-Cortex* | *25* | *2* | *28* | *18* |
| *PG-Sentinel* | *19* | *2* | *25* | *19* |
| *PG-Analytics* | *325* | *2* | *880* | *284* |
| *PG-Infrastructure* | *69* | *4* | *195* | *86* |
| *PG-APP-Core* | *26* | *3* | *89* | *15* |
| *PG-Shared-Lib* | *19* | *3* | *29* | *16* |
| *PG-Edge-Container* | *13* | *1* | *48* | *22* |
| *PG-Airflow-DAGs* | *16* | *3* | *12* | *9* |
- ### *Summary*
  - *👀 Views ( 14 Days ) :　940*
  - *👤 Unique Visitors :　43*
  - *📥 Clones ( 14 Days ) :　2283*
  - *👤 Unique Cloners :　851*
<!-- traffic:end -->

<br>

### *📈　Monthly Growth Analytics*

<!-- growth:start -->
> _Statistical Scope :　**2026-07**_
>
> _Generated at [ UTC+0 ] :　2026-07-05T17:31:17_

| *📁 Repository* | *⭐ Stars ↕* | *👀 Forks ↕* | *📥 Open Issues ↕* |
|:--|--:|--:|--:|
| *Platform-Genesis* | *+0* | *+0* | *+0* |
| *PG-Core* | *+0* | *+0* | *+0* |
| *PG-Synapse* | *+0* | *+0* | *+0* |
| *PG-Cortex* | *+0* | *+0* | *+0* |
| *PG-Sentinel* | *+0* | *+0* | *+0* |
| *PG-Analytics* | *+0* | *+0* | *+0* |
| *PG-Infrastructure* | *+0* | *+0* | *+0* |
| *PG-APP-Core* | *+0* | *+0* | *+0* |
| *PG-Shared-Lib* | *+0* | *+0* | *+0* |
| *PG-Edge-Container* | *+0* | *+0* | *+0* |
| *PG-Airflow-DAGs* | *+0* | *+0* | *+0* |
<!-- growth:end -->


<br><br><br>