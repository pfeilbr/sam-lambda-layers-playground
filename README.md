# sam-lambda-layers-playground

learn [SAM lambda layers](https://aws.amazon.com/blogs/compute/working-with-aws-lambda-and-lambda-layers-in-aws-sam/)

## Running Example

```sh
cd lambda-layer-python

sam build

# run lambda with layer locally
# `--force-image-build` to clear out layer cache
sam local invoke --force-image-build

# start local api endpoint
sam local start-api --force-image-build
curl http://127.0.0.1:3000/
```

## Resources

* [Working with AWS Lambda and Lambda Layers in AWS SAM](https://aws.amazon.com/blogs/compute/working-with-aws-lambda-and-lambda-layers-in-aws-sam/)