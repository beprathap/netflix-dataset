- Installation
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install dbt-snowflake
- Create dbt profile
    mkdir ~/.dbt # its a hidden folder
    dbt init netflix
    enter a number: 1
- In case error while connecting to snowflake, update everything
    pip install --upgrade snowflake-connector-python

- To run the project
    dbt debug
    dbt run
    dbt test
    dbt docs generate
    dbt docs serve
- To see the lineage graph
    dbt docs serve
- To see the models
    dbt list