FROM python:3.10-slim

# ติดตั้ง Apache Airflow
RUN pip install apache-airflow

# สร้าง directory สำหรับ Airflow
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดไปยัง container
COPY . /app

# ติดตั้ง requirements (ถ้ามี)
RUN pip install -r requirements.txt

# คำสั่งเริ่มต้น: เปิด bash shell
CMD ["bash"]
