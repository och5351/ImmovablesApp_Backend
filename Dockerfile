FROM openjdk:11-jre-alpine
COPY target/*.jar app.jar
CMD ["java","-jar","/app.jar"]