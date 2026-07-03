<a href='https://github.com/Junwu0615/Platform Genesis'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Platform Genesis.svg'>
[![Back to HomePage](https://img.shields.io/badge/%F0%9F%8C%90_Back_to-HomePage-blue?style=flat-square)](https://github.com/Junwu0615/Platform-Genesis)

## *⭐ Platform Genesis Universe Analytics ⭐*

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
| *👀 Total Views* | *411* |
| *📥 Total Clones* | *1595* |
| *👤 Unique Visitors* | *32* |
| *👤 Unique Clones* | *598* |
> _Note : Metrics are aggregated across all tracked repositories._
>
> _Generated at [ UTC+0 ] : 2026-07-03T23:15:56_
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->
 | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *👀 Views* | *📥 Clones* |
 |:--|--:|--:|--:|--:|
 | *Platform-Genesis* | *2* | *0* | *269* | *737* |
 | *PG-Core* | *1* | *0* | *0* | *0* |
 | *PG-Synapse* | *1* | *0* | *0* | *0* |
 | *PG-Cortex* | *1* | *0* | *0* | *0* |
 | *PG-Sentinel* | *1* | *0* | *0* | *0* |
 | *PG-Analytics* | *1* | *0* | *0* | *0* |
 | *PG-Infrastructure* | *1* | *0* | *111* | *614* |
 | *PG-APP-Core* | *1* | *0* | *12* | *122* |
 | *PG-Shared-Lib* | *1* | *0* | *6* | *33* |
 | *PG-Edge-Container* | *1* | *0* | *5* | *60* |
 | *PG-Airflow-DAGs* | *1* | *0* | *8* | *29* |
- ### *Summary*
  - *📁 Repository : 11*
  - *⭐ Stars : 12*
  - *🍴 Forks : 0*
  - *👀 Views ( 14 days ) : 411*
  - *📥 Clones ( 14 days ) : 1595*
> _Generated at [ UTC+0 ] : 2026-07-03T23:15:56_
<!-- dashboard:end -->

<br>

### *🔍　Traffic Analytics*

<!-- traffic:start -->
| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |
|:--|--:|--:|--:|--:|
| *Platform-Genesis* | *269* | *19* | *737* | *273* |
| *PG-Core* | *0* | *0* | *0* | *0* |
| *PG-Synapse* | *0* | *0* | *0* | *0* |
| *PG-Cortex* | *0* | *0* | *0* | *0* |
| *PG-Sentinel* | *0* | *0* | *0* | *0* |
| *PG-Analytics* | *0* | *0* | *0* | *0* |
| *PG-Infrastructure* | *111* | *4* | *614* | *243* |
| *PG-APP-Core* | *12* | *3* | *122* | *24* |
| *PG-Shared-Lib* | *6* | *2* | *33* | *17* |
| *PG-Edge-Container* | *5* | *1* | *60* | *27* |
| *PG-Airflow-DAGs* | *8* | *3* | *29* | *14* |
- ### *Summary*
  - *👀 Views ( 14 Days ) : 411*
  - *👤 Unique Visitors : 32*
  - *📥 Clones ( 14 Days ) : 1595*
  - *👤 Unique Cloners : 598*
> _Generated at [ UTC+0 ] : 2026-07-03T23:15:56_
<!-- traffic:end -->

<br>

### *📈　Growth Analytics*

<!-- growth:start -->
| *📁 Repository* | *⭐ Stars ↑* | *👀 Views ↑* | *📥 Clones ↑* |
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
> _Statistical Scope : **2026-07** → **2026-07**_
>
> _Initial startup time data ( March – June 2026 ) was not captured due to the absence of a record-keeping script._
>
> _Generated at [ UTC+0 ] : 2026-07-03T23:15:56_
<!-- growth:end -->


<br><br><br>