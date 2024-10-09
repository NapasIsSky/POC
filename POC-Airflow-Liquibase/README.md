## Source Command

```
docker exec -it source-mock_source-1 mysql -uuser -puserpassword sourcedb
```

```
CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  position VARCHAR(100),
  salary DECIMAL(10,2)
);
```

```
INSERT INTO employees (name, position, salary) VALUES
('Alice', 'Manager', 7000.50),
('Bob', 'Developer', 5000.00),
('Charlie', 'Designer', 4000.00);
```

## Destination command

```
docker network create \
--driver bridge \
--subnet 172.20.0.0/16 \
--gateway 172.20.0.1 \
poc-airflow-liquibase-destination
docker network inspect poc-airflow-liquibase-destination
```

```
docker exec -it postgresql-postgres-1 psql -U user destinationdb
```

```
CREATE TABLE employees (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
name VARCHAR(225),
job_title VARCHAR(225),
monthly_salary BIGINT
);
```
