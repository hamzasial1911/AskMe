# from contextlib import asynccontextmanager

# from fastapi import FastAPI


# @asynccontextmanager
# async def lifespan(_app: FastAPI):
#     # startup, includes dev refresh

#     # start taking requests
#     yield
#     # cleanup


# app = FastAPI(
#     title="AskMe API",
#     version="0.1.0",
#     # dependencies= [Depends()],
#     lifespan=lifespan,
# )


# @app.get("/health")
# def healthcheck():
#     return 200


# @app.get("/", status_code=200)
# def helloworld():
#     return "<h1>Hello World</h1>"
