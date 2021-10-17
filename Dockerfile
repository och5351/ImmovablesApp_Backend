FROM openjdk:11-jre-alpine
VOLUME /tmp
ADD ./springjava/build/libs/springjava-0.0.1-SNAPSHOT.jar app.jar
ENV JAVA_OPTS=""
ENTRYPOINT ["java","-jar","/app.jar"]