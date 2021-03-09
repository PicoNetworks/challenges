## Data Engineer Challenge

For this challenge, you will use a subset of the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce). The link provides detailed information about the dataset, including the data schema.


### Development Environment Setup

We are providing you with a docker-compose to simplify the setup. It will start the database and a Jupyter Lab server.

 You can complete the challenge using either MariaDB or PostgreSQL. The docker-compose.yml supports both.

- MariaDB: `docker-compose up mariadb lab`
- PostgreSQL: `docker-compose up postgres lab`

Please take note the Jupyter Lab URL at the end of the startup process: you will need it later!

In both cases, an empty database named `olist` will be created. The database credentials are in the `docker-compose.yml` file.

Download the dataset from https://www.kaggle.com/olistbr/brazilian-ecommerce/download and unzip the files into the `work/csv` folder.

The `lab` service uses the `jupyter/scipy-notebook` image, which should contain all packages you may need for the challenge.

If you are more comfortable using some alternative library, add it to `work/requirements.txt` and restart your dev environment.

Feel free to change the docker-compose.yml and use other images for Jupyter Lab.


### Create the database schema

Your first task is to create the database schema. After selecting your database flavor, create the tables according to the Data schema available in the Description section of the [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce).

Simplify the table names by removing the `olist_` prefix and the `_dataset` suffix. Eg: `olist_customers_dataset.csv` should become the `customers` table.

The following tables are required in the schema:

- customers
- sellers
- products
- orders
- order_items
- order_reviews

We expect the schema to define at least the primary keys and foreign keys. Any other indices or constraints are optional.

Write the SQL statements for creating the schema to the `sql/schema.sql` file.

### Completing the challenge

Open `challenge.ipynb` in Jupyter Lab and follow the instructions.

Fork the repo and send us a link to your GitHub account as your submission.

### Have fun!
