# เริ่มต้นด้วย Official Liquibase Image
FROM liquibase/liquibase:latest

# ติดตั้ง MySQL และ PostgreSQL drivers ผ่าน LPM (Liquibase Package Manager)
RUN lpm update # อัปเดต LPM ก่อนติดตั้ง drivers
RUN lpm add mysql --global
RUN lpm add postgresql --global

RUN rm /liquibase/internal/lib/postgresql.jar

# ตรวจสอบการติดตั้งและเวอร์ชันของ Liquibase
RUN liquibase --version
