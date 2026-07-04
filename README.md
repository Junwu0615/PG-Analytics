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
collect.py
   ↓
data/latest/*.json
( 最新快照 )


# STAGE. 2
export_history.py
   ↓
history/YYYY-MM-history.csv
( 每日快照累積 / 按月分區 )


# STAGE. 3
generate_report.py
   ↓
data/summary.json
( 所有 Repo 最新統計總覽 )
   ↓
summary.md
dashboard.md
traffic.md
growth.md


# STAGE. 4
sync_readme.py
   ↓
README.md
( 所有 Report 渲染至首頁 )
```

</ul>
</details>

<br>

### *📋　Repository Summary Report*

<!-- summary:start -->
| *📐 Metric* | *🧮 Value* |
|:--|--:|
| *📁 Total Repositories* | *11* |
| *⭐ Total Stars* | *12* |
| *🍴 Total Forks* | *0* |
| *👀 Total Views* | *525* |
| *📥 Total Clones* | *1670* |
| *👤 Unique Visitors* | *34* |
| *👤 Unique Clones* | *641* |
> _Note : Metrics are aggregated across all tracked repositories._
>
> _Generated at [ UTC+0 ] : 2026-07-04T06:20:39_
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->
 | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *👀 Views* | *📥 Clones* |
 |:--|--:|--:|--:|--:|
 | *Platform-Genesis* | *2* | *0* | *327* | *781* |
 | *PG-Core* | *1* | *0* | *0* | *0* |
 | *PG-Synapse* | *1* | *0* | *11* | *30* |
 | *PG-Cortex* | *1* | *0* | *0* | *0* |
 | *PG-Sentinel* | *1* | *0* | *12* | *23* |
 | *PG-Analytics* | *1* | *0* | *0* | *0* |
 | *PG-Infrastructure* | *1* | *0* | *111* | *614* |
 | *PG-APP-Core* | *1* | *0* | *24* | *113* |
 | *PG-Shared-Lib* | *1* | *0* | *17* | *28* |
 | *PG-Edge-Container* | *1* | *0* | *10* | *57* |
 | *PG-Airflow-DAGs* | *1* | *0* | *13* | *24* |
- ### *Summary*
  - *📁 Repository : 11*
  - *⭐ Stars : 12*
  - *🍴 Forks : 0*
  - *👀 Views ( 14 days ) : 525*
  - *📥 Clones ( 14 days ) : 1670*
> _Generated at [ UTC+0 ] : 2026-07-04T06:20:39_
<!-- dashboard:end -->

<br>

### *🔍　Traffic Analytics*

<!-- traffic:start -->
| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |
|:--|--:|--:|--:|--:|
| *Platform-Genesis* | *327* | *18* | *781* | *290* |
| *PG-Core* | *0* | *0* | *0* | *0* |
| *PG-Synapse* | *11* | *1* | *30* | *18* |
| *PG-Cortex* | *0* | *0* | *0* | *0* |
| *PG-Sentinel* | *12* | *1* | *23* | *17* |
| *PG-Analytics* | *0* | *0* | *0* | *0* |
| *PG-Infrastructure* | *111* | *4* | *614* | *243* |
| *PG-APP-Core* | *24* | *3* | *113* | *21* |
| *PG-Shared-Lib* | *17* | *3* | *28* | *15* |
| *PG-Edge-Container* | *10* | *1* | *57* | *25* |
| *PG-Airflow-DAGs* | *13* | *3* | *24* | *12* |
- ### *Summary*
  - *👀 Views ( 14 Days ) : 525*
  - *👤 Unique Visitors : 34*
  - *📥 Clones ( 14 Days ) : 1670*
  - *👤 Unique Cloners : 641*
> _Generated at [ UTC+0 ] : 2026-07-04T06:20:39_
<!-- traffic:end -->

<br>

### *📈　Monthly Growth Analytics*

<!-- growth:start -->
| *📁 Repository* | *⭐ Stars ↑* | *👀 Views ↑* | *📥 Clones ↑* |
|:--|--:|--:|--:|
| *Platform-Genesis* | *+0* | *+58* | *+44* |
| *PG-Core* | *+0* | *+0* | *+0* |
| *PG-Synapse* | *+0* | *+11* | *+30* |
| *PG-Cortex* | *+0* | *+0* | *+0* |
| *PG-Sentinel* | *+0* | *+12* | *+23* |
| *PG-Analytics* | *+0* | *+0* | *+0* |
| *PG-Infrastructure* | *+0* | *+0* | *+0* |
| *PG-APP-Core* | *+0* | *+12* | *-9* |
| *PG-Shared-Lib* | *+0* | *+11* | *-5* |
| *PG-Edge-Container* | *+0* | *+5* | *-3* |
| *PG-Airflow-DAGs* | *+0* | *+5* | *-5* |
> _Statistical Scope : **2026-07** → **2026-07**_
>
> _Generated at [ UTC+0 ] : 2026-07-04T06:20:39_
<!-- growth:end -->


<br><br><br>