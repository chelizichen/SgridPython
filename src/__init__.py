from sanic import Sanic, Request, HTTPResponse, json

from src.utils.ret import R

serverName = "SgridPythonChatServer"
app = Sanic(serverName)


@app.post("/ask")
async def ask_question(request: Request) -> HTTPResponse:
    return json(R.success("ok"))


@app.post("/with_session")
async def with_session(request: Request) -> HTTPResponse:
    return json(R.success("ok"))
