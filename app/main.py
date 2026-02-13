from fastapi import FastAPI
from app.routers import titles, thumbnails, descriptions, seo, workflows, projects, images, ai, youtube
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

app.include_router(titles.router, prefix="/titles", tags=["Títulos"])
app.include_router(thumbnails.router, prefix="/thumbnails", tags=["Miniaturas"])
app.include_router(descriptions.router, prefix="/descriptions", tags=["Descripciones"])
app.include_router(seo.router, prefix="/seo", tags=["SEO"])
app.include_router(workflows.router, prefix="/workflows", tags=["Flujos"])
app.include_router(projects.router, prefix="/projects", tags=["Proyectos"])
app.include_router(images.router, prefix="/images", tags=["Imagen"])
app.include_router(ai.router, prefix="/ai", tags=["IA Generativa (Gemini)"])
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube Analytics"])

@app.get("/")
def root():
    return {"message": "OEMB Studio API", "docs": "/docs"}