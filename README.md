<a href='https://github.com/Junwu0615/Platform Genesis'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Platform Genesis.svg'>
[![Back to HomePage](https://img.shields.io/badge/%F0%9F%8C%90_Back_to-HomePage-blue?style=flat-square)](https://github.com/Junwu0615/Platform-Genesis)

## *⭐ Platform Genesis Universe Analytics ⭐*
> 🧟‍♂️ _Initial startup time data ( March – July 2026 ) was not_
> _captured due to the absence of a record-keeping script._
> 
> 🤕 _Recording officially began on 2026-07-23_

<!-- update_time:start -->
>
> _Generated at [ UTC+0 ] :　2026-07-28T17:44:19_

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
| *⭐ Total Stars* | *13* |
| *🍴 Total Forks* | *0* |
| *📩 Total Commit* | *1368* |
| *📦 Size ( MB )* | *72.61* |
| *👀 Total Views* | *603* |
| *👤 Total Unique Visitors* | *34* |
| *📥 Total Clones* | *796* |
| *👤 Total Unique Cloners* | *449* |
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->

 | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *📩 Commit* | *📦 Size<br>( MB )* | *📝 Updated* | *📅 Created* |
 |:--|--:|--:|--:|--:|--:|--:|
 | _**[Platform-Genesis](https://github.com/Junwu0615/Platform-Genesis)**_ | *3* | *0* | *608* | *57.94* | *2026-07-28* | *2026-03-20* |
 | _**[PG-Core](https://github.com/Junwu0615/PG-Core)**_ | *1* | *0* | *54* | *9.08* | *2026-07-23* | *2026-07-03* |
 | _**[PG-Synapse](https://github.com/Junwu0615/PG-Synapse)**_ | *1* | *0* | *4* | *0.01* | *2026-07-23* | *2026-07-03* |
 | _**[PG-Cortex](https://github.com/Junwu0615/PG-Cortex)**_ | *1* | *0* | *6* | *0.01* | *2026-07-23* | *2026-07-03* |
 | _**[PG-Sentinel](https://github.com/Junwu0615/PG-Sentinel)**_ | *1* | *0* | *3* | *0.00* | *2026-07-23* | *2026-07-03* |
 | _**[PG-Analytics](https://github.com/Junwu0615/PG-Analytics)**_ | *1* | *0* | *193* | *0.32* | *2026-07-27* | *2026-07-03* |
 | _**[PG-Infrastructure](https://github.com/Junwu0615/PG-Infrastructure)**_ | *1* | *0* | *363* | *4.98* | *2026-07-23* | *2026-05-08* |
 | _**[PG-APP-Core](https://github.com/Junwu0615/PG-APP-Core)**_ | *1* | *0* | *63* | *0.12* | *2026-07-23* | *2026-05-08* |
 | _**[PG-Shared-Lib](https://github.com/Junwu0615/PG-Shared-Lib)**_ | *1* | *0* | *21* | *0.05* | *2026-07-23* | *2026-05-08* |
 | _**[PG-Edge-Container](https://github.com/Junwu0615/PG-Edge-Container)**_ | *1* | *0* | *25* | *0.04* | *2026-07-23* | *2026-05-08* |
 | _**[PG-Airflow-DAGs](https://github.com/Junwu0615/PG-Airflow-DAGs)**_ | *1* | *0* | *28* | *0.06* | *2026-07-23* | *2026-05-08* |
<!-- dashboard:end -->

<br>

### *🔍　Traffic Analytics*

<!-- traffic:start -->
> _Traffic in the past **14 Days**_

| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |
|:--|--:|--:|--:|--:|
| _**[Platform-Genesis](https://github.com/Junwu0615/Platform-Genesis)**_ | *251* | *10* | *242* | *121* |
| _**[PG-Core](https://github.com/Junwu0615/PG-Core)**_ | *116* | *6* | *95* | *53* |
| _**[PG-Synapse](https://github.com/Junwu0615/PG-Synapse)**_ | *6* | *2* | *16* | *15* |
| _**[PG-Cortex](https://github.com/Junwu0615/PG-Cortex)**_ | *7* | *2* | *20* | *16* |
| _**[PG-Sentinel](https://github.com/Junwu0615/PG-Sentinel)**_ | *6* | *2* | *15* | *14* |
| _**[PG-Analytics](https://github.com/Junwu0615/PG-Analytics)**_ | *102* | *4* | *245* | *114* |
| _**[PG-Infrastructure](https://github.com/Junwu0615/PG-Infrastructure)**_ | *34* | *3* | *57* | *42* |
| _**[PG-APP-Core](https://github.com/Junwu0615/PG-APP-Core)**_ | *18* | *2* | *38* | *25* |
| _**[PG-Shared-Lib](https://github.com/Junwu0615/PG-Shared-Lib)**_ | *16* | *1* | *21* | *15* |
| _**[PG-Edge-Container](https://github.com/Junwu0615/PG-Edge-Container)**_ | *15* | *1* | *20* | *15* |
| _**[PG-Airflow-DAGs](https://github.com/Junwu0615/PG-Airflow-DAGs)**_ | *32* | *1* | *27* | *19* |
- ### *Summary*
  - *👀 Views :　603*
  - *👤 Unique Visitors :　34*
  - *📥 Clones :　796*
  - *👤 Unique Cloners :　449*
<!-- traffic:end -->

<br>

### *📈　Monthly Growth Analytics*

<!-- growth:start -->
> _Statistical Scope : **2026-07**_

| *📁 Repository* | *⭐ Stars ↕* | *🍴 Forks ↕* | *💡 Open Issues ↕* | *👀 Views ↕* | *📥 Clones ↕* |
|:--|--:|--:|--:|--:|--:|
| _**[Platform-Genesis](https://github.com/Junwu0615/Platform-Genesis)**_ | *+0* | *+0* | *+0* | *281* | *307* | 
| _**[PG-Core](https://github.com/Junwu0615/PG-Core)**_ | *+0* | *+0* | *+0* | *127* | *121* | 
| _**[PG-Synapse](https://github.com/Junwu0615/PG-Synapse)**_ | *+0* | *+0* | *+0* | *7* | *18* | 
| _**[PG-Cortex](https://github.com/Junwu0615/PG-Cortex)**_ | *+0* | *+0* | *+0* | *7* | *24* | 
| _**[PG-Sentinel](https://github.com/Junwu0615/PG-Sentinel)**_ | *+0* | *+0* | *+0* | *6* | *18* | 
| _**[PG-Analytics](https://github.com/Junwu0615/PG-Analytics)**_ | *+0* | *+0* | *+0* | *103* | *272* | 
| _**[PG-Infrastructure](https://github.com/Junwu0615/PG-Infrastructure)**_ | *+0* | *+0* | *+0* | *39* | *103* | 
| _**[PG-APP-Core](https://github.com/Junwu0615/PG-APP-Core)**_ | *+0* | *+0* | *+0* | *24* | *81* | 
| _**[PG-Shared-Lib](https://github.com/Junwu0615/PG-Shared-Lib)**_ | *+0* | *+0* | *+0* | *17* | *22* | 
| _**[PG-Edge-Container](https://github.com/Junwu0615/PG-Edge-Container)**_ | *+0* | *+0* | *+0* | *15* | *21* | 
| _**[PG-Airflow-DAGs](https://github.com/Junwu0615/PG-Airflow-DAGs)**_ | *+0* | *+0* | *+0* | *33* | *29* | 
<!-- growth:end -->


<br><br><br>