<a href='https://github.com/Junwu0615/Platform Genesis'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Platform Genesis.svg'>
[![Back to HomePage](https://img.shields.io/badge/%F0%9F%8C%90_Back_to-HomePage-blue?style=flat-square)](https://github.com/Junwu0615/Platform-Genesis)

## *⭐ Platform Genesis Universe Analytics ⭐*
> _🧟‍♂️ Initial startup time data ( March – June 2026 ) was not_ 
> _captured due to the absence of a record-keeping script._
<!-- update_time:start -->
>
> _Generated at [ UTC+0 ] :　2026-07-22T17:38:30_

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
| *📦 Size (MB)* | *63.51* |
| *👀 Total Views* | *238* |
| *👤 Total Unique Visitors* | *25* |
| *📥 Total Clones* | *515* |
| *👤 Total Unique Cloners* | *267* |
<!-- summary:end -->

<br>

### *📊　Repository Dashboard*

<!-- dashboard:start -->

 | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *📦 Size (MB)* | *📝 Last Updated* | *📅 Creation Date* |
 |:--|--:|--:|--:|--:|--:|
 | *[Platform-Genesis](https://github.com/Junwu0615/Platform-Genesis)* | *2* | *0* | *53.43* | *2026-07-22* | *2026-03-20* |
 | *[PG-Core](https://github.com/Junwu0615/PG-Core)* | *1* | *0* | *4.59* | *2026-07-22* | *2026-07-03* |
 | *[PG-Synapse](https://github.com/Junwu0615/PG-Synapse)* | *1* | *0* | *0.00* | *2026-07-05* | *2026-07-03* |
 | *[PG-Cortex](https://github.com/Junwu0615/PG-Cortex)* | *1* | *0* | *0.01* | *2026-07-05* | *2026-07-03* |
 | *[PG-Sentinel](https://github.com/Junwu0615/PG-Sentinel)* | *1* | *0* | *0.00* | *2026-07-05* | *2026-07-03* |
 | *[PG-Analytics](https://github.com/Junwu0615/PG-Analytics)* | *1* | *0* | *0.25* | *2026-07-22* | *2026-07-03* |
 | *[PG-Infrastructure](https://github.com/Junwu0615/PG-Infrastructure)* | *1* | *0* | *4.97* | *2026-07-22* | *2026-05-08* |
 | *[PG-APP-Core](https://github.com/Junwu0615/PG-APP-Core)* | *1* | *0* | *0.12* | *2026-07-22* | *2026-05-08* |
 | *[PG-Shared-Lib](https://github.com/Junwu0615/PG-Shared-Lib)* | *1* | *0* | *0.05* | *2026-07-21* | *2026-05-08* |
 | *[PG-Edge-Container](https://github.com/Junwu0615/PG-Edge-Container)* | *1* | *0* | *0.03* | *2026-07-21* | *2026-05-08* |
 | *[PG-Airflow-DAGs](https://github.com/Junwu0615/PG-Airflow-DAGs)* | *1* | *0* | *0.06* | *2026-06-22* | *2026-05-08* |
<!-- dashboard:end -->

<br>

### *🔍　Traffic Analytics*

<!-- traffic:start -->
> _Traffic in the past **14 Days**_

| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |
|:--|--:|--:|--:|--:|
| *[Platform-Genesis](https://github.com/Junwu0615/Platform-Genesis)* | *145* | *7* | *173* | *72* |
| *[PG-Core](https://github.com/Junwu0615/PG-Core)* | *38* | *3* | *58* | *29* |
| *[PG-Synapse](https://github.com/Junwu0615/PG-Synapse)* | *3* | *2* | *11* | *10* |
| *[PG-Cortex](https://github.com/Junwu0615/PG-Cortex)* | *2* | *1* | *12* | *10* |
| *[PG-Sentinel](https://github.com/Junwu0615/PG-Sentinel)* | *2* | *1* | *11* | *10* |
| *[PG-Analytics](https://github.com/Junwu0615/PG-Analytics)* | *4* | *2* | *84* | *45* |
| *[PG-Infrastructure](https://github.com/Junwu0615/PG-Infrastructure)* | *26* | *2* | *75* | *32* |
| *[PG-APP-Core](https://github.com/Junwu0615/PG-APP-Core)* | *9* | *2* | *63* | *40* |
| *[PG-Shared-Lib](https://github.com/Junwu0615/PG-Shared-Lib)* | *4* | *2* | *12* | *7* |
| *[PG-Edge-Container](https://github.com/Junwu0615/PG-Edge-Container)* | *2* | *1* | *10* | *7* |
| *[PG-Airflow-DAGs](https://github.com/Junwu0615/PG-Airflow-DAGs)* | *3* | *2* | *6* | *5* |
- ### *Summary*
  - *👀 Views :　238*
  - *👤 Unique Visitors :　25*
  - *📥 Clones :　515*
  - *👤 Unique Cloners :　267*
<!-- traffic:end -->

<br>

### *📈　Monthly Growth Analytics*

<!-- growth:start -->
> _Statistical Scope :　**2026-07**_

| *📁 Repository* | *⭐ Stars ↕* | *🍴 Forks ↕* | *💡 Open Issues ↕* | *👀 Views ↕<br>( 14 Days )* | *📥 Clones ↕<br>( 14 Days )* |
|:--|--:|--:|--:|--:|--:|
| *[Platform-Genesis](https://github.com/Junwu0615/Platform-Genesis)* | *+0* | *+0* | *+0* |*-136* | *-765* | 
| *[PG-Core](https://github.com/Junwu0615/PG-Core)* | *+0* | *+0* | *+0* |*+41* | *+87* | 
| *[PG-Synapse](https://github.com/Junwu0615/PG-Synapse)* | *+0* | *+0* | *+0* |*+5* | *+21* | 
| *[PG-Cortex](https://github.com/Junwu0615/PG-Cortex)* | *+0* | *+0* | *+0* |*+3* | *+22* | 
| *[PG-Sentinel](https://github.com/Junwu0615/PG-Sentinel)* | *+0* | *+0* | *+0* |*+3* | *+21* | 
| *[PG-Analytics](https://github.com/Junwu0615/PG-Analytics)* | *+0* | *+0* | *+0* |*+6* | *+129* | 
| *[PG-Infrastructure](https://github.com/Junwu0615/PG-Infrastructure)* | *+0* | *+0* | *+0* |*-87* | *-750* | 
| *[PG-APP-Core](https://github.com/Junwu0615/PG-APP-Core)* | *+0* | *+0* | *+0* |*-4* | *-43* | 
| *[PG-Shared-Lib](https://github.com/Junwu0615/PG-Shared-Lib)* | *+0* | *+0* | *+0* |*-2* | *-31* | 
| *[PG-Edge-Container](https://github.com/Junwu0615/PG-Edge-Container)* | *+0* | *+0* | *+0* |*-3* | *-70* | 
| *[PG-Airflow-DAGs](https://github.com/Junwu0615/PG-Airflow-DAGs)* | *+0* | *+0* | *+0* |*-6* | *-32* | 
<!-- growth:end -->


<br><br><br>