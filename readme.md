# Kafka Project

This is a solution for setting up a Kafka project with Elasticsearch for processing and storing cryptocurrency data. The project utilizes Docker containers to easily set up and manage the required services.

## Prerequisites

Make sure you have the following software installed on your machine:

- Docker
- Docker Compose

## Getting Started

To get started with the Kafka project, follow the steps below:

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/marcelpinheiro/kafka-project.git
   ```

2. Navigate to the project directory:
   ```
   cd kafka-project
   ```

3. Start the Docker containers using Docker Compose:
   ```
   docker-compose up -d
   ```

   This command will start the following services:

   - ZooKeeper: Apache Kafka dependency for maintaining coordination between brokers.
   - Broker: Apache Kafka broker that handles the messaging infrastructure.
   - Elasticsearch: A distributed search and analytics engine for storing cryptocurrency data.
   - Kibana: An open-source data visualization and exploration tool for Elasticsearch.

   The containers will be created and started in the background.

4. Wait for the services to start up. You can monitor the logs of each container using the following command:
   ```
   docker-compose logs -f
   ```

   This will display the logs of all the services. Press `Ctrl + C` to stop following the logs.

5. Once the services are up and running, you can access Kibana by opening your web browser and navigating to [http://localhost:5601](http://localhost:5601).

6. Use Kibana to explore and visualize the cryptocurrency data stored in Elasticsearch.

## Customization

If you need to customize any configuration parameters or add additional services to the project, you can modify the `docker-compose.yml` file.

- To change the version of the services, update the `image` tag for each service.
- To expose different ports for the services, modify the `ports` section for each container.
- To add additional environment variables for a service, add or modify the `environment` section for that service.

## Cleanup

To stop and remove the Docker containers associated with the Kafka project, run the following command from the project directory:

```
docker-compose down -v
```

This will stop the containers and remove them from your system.

## Conclusion

With this Kafka project setup, you can easily process and store cryptocurrency data using Apache Kafka and Elasticsearch. Feel free to explore the code and adapt it to your specific needs. If you have any questions or issues, please refer to the GitHub repository for support. Happy coding!
