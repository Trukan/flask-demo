# flask_demo

## Development

## Building for production

## Testing

## Using Docker to simplify development (optional)

A number of docker-compose configuration are available in the [src/docker](src/docker) folder to launch required third party services.

For example, to start in a docker container, run:

    docker-compose -f src/docker/app.yml up -d
    
Or build then start:
    
    docker build -t flask_demo:latest -f src/docker/Dockerfile .

    docker run --name flask_demo -d -p 8000:5000 --rm flask_demo:latest

To stop it and remove the container, run:

    docker-compose -f src/docker/app.yml down
