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
poc-liquibase-destination
docker network inspect poc-liquibase-destination
```

```
docker exec -it postgresql-postgres-1 psql -U user destinationdb
```

```
CREATE TABLE employees (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
emp_id BIGINT,
name VARCHAR(225),
job_title VARCHAR(225),
monthly_salary BIGINT
);
```

```
docker run --rm -v /Users/Napas/Documents/POC/POC-Liquibase/destination/liquibase/changelog:/liquibase/changelog liquibase/liquibase --defaults-file=/liquibase/changelog/liquibase.docker.properties update
```
