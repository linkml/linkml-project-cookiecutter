################################################
#### Commands for building the Docker image ####
################################################

IM=linkml/linkml-project-cookiecutter
VERSION=0.1.0

docker-build-no-cache:
	@docker build --no-cache -t $(IM):$(VERSION) . \
	&& docker tag $(IM):$(VERSION) $(IM):latest

docker-build:
	@docker build -t $(IM):$(VERSION) . \
	&& docker tag $(IM):$(VERSION) $(IM):latest

docker-build-use-cache-dev:
	@docker build -t $(DEV):$(VERSION) . \
	&& docker tag $(DEV):$(VERSION) $(DEV):latest

docker-clean:
	docker kill $(IM) || echo not running ;
	docker rm $(IM) || echo not made 

docker-publish-no-build:
	@docker push $(IM):$(VERSION) \
	&& docker push $(IM):latest

docker-publish-dev-no-build:
	@docker push $(DEV):$(VERSION) \
	&& docker push $(DEV):latest

docker-publish: docker-build
	@docker push $(IM):$(VERSION) \
	&& docker push $(IM):latest

docker-run:
	docker run  -v $(PWD):/work -w /work -v /tmp:/tmp -v ~/.ssh:/work/.ssh -ti $(IM):$(VERSION) 

docker-shell:
	docker run  -v $(PWD):/work -w /work -v /tmp:/tmp -ti $(IM):$(VERSION) bash
