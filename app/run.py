import os
import uvicorn

MODE = os.getenv("MODE", "api")

if MODE == "pipeline":
    from app.main import run
    run()

elif MODE == "dashboard":
    from app.dashboard import run
    run()

else:
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000)
