FROM adoptopenjdk/openjdk11:jdk-11.0.11_9-alpine-slim
VOLUME /tmp
ADD ./build/libs/springjava-0.0.1-SNAPSHOT.jar app.jar
ENV JAVA_OPTS=""
ENTRYPOINT ["java","-jar","/app.jar"]