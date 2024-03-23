CAUTION: Using docker within docker could bear some security risks.
> Although running Docker inside Docker is generally not recommended, there are some legitimate use cases, such as development of Docker itself. (https://hub.docker.com/_/docker/)

However using host's `docker.sock` from inside a container could be considered as secure (Docker outside of Docker: DooD). See:
[https://medium.com/@rashmi160403/securely-running-docker-in-docker-a-comprehensive-guide-cb6efb5b745f](https://medium.com/@rashmi160403/securely-running-docker-in-docker-a-comprehensive-guide-cb6efb5b745f)

See also: 
[https://forums.docker.com/t/execute-command-from-a-container-to-another-container/19492](https://forums.docker.com/t/execute-command-from-a-container-to-another-container/19492) 

[https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)

`docker compose up -d`
`docker compose exec backup sh ./clean-backup.sh`