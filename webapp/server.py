from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", context = {"request": request})

@app.get("/chat/character/categories/")
async def get_character_categories():
    return {"categories": [{"name": "Games", "description": "Games"}, {"name": "Image Generating", "description": "Image Generating"}, {"name": "VTuber", "description": "Vtubers"}, {"name": "Game Characters", "description": "Game Characters"}, {"name": "Helpers", "description": "Helpers"}, {"name": "Anime", "description": "Anime characters"}, {"name": "Famous People", "description": "Famous People"}, {"name": "Action", "description": "Action & Adventure"}, {"name": "Animals", "description": "Animals"}, {"name": "Fantasy", "description": "Fantasy"}, {"name": "Language Learning", "description": "Language Learning"}, {"name": "Discussion", "description": "Discussion"}, {"name": "Movies & TV", "description": "Movies & TV"}, {"name": "Religion", "description": "Religion"}, {"name": "Anime Game Characters", "description": "Game characters from Anime"}, {"name": "Knowledge", "description": "Knowledge & Research"}, {"name": "Entertainment", "description": "Entertainment"}, {"name": "Advice", "description": "Advice"}, {"name": "Debate", "description": "Debate"}, {"name": "Technology", "description": "Technology"}, {"name": "Comedy", "description": "Comedy & Humor"}, {"name": "Chinese", "description": "Chinese Characters"}, {"name": "Philosophy", "description": "Philosophy"}, {"name": "Cooperative", "description": "Cooperative"}, {"name": "Music", "description": "Music"}, {"name": "Science Fiction", "description": "Science Fiction"}, {"name": "Politics", "description": "Politics"}, {"name": "Art", "description": "Art"}, {"name": "Books", "description": "Books, Literature & Poetry"}, {"name": "Mystery", "description": "Mystery & Horror"}, {"name": "Science", "description": "Science"}, {"name": "Decisions", "description": "Decisions"}, {"name": "Nature", "description": "Nature & Outdoors"}, {"name": "Pets", "description": "Pets"}, {"name": "Business", "description": "Business"}, {"name": "Family", "description": "Family"}, {"name": "History", "description": "History"}, {"name": "Drama", "description": "Drama"}, {"name": "Motivation", "description": "Motivation"}, {"name": "Space", "description": "Space"}, {"name": "English", "description": "English"}, {"name": "Food", "description": "Food & Cooking"}, {"name": "Education", "description": "Education & Learning"}, {"name": "Writing", "description": "Writing"}, {"name": "Language", "description": "Language & Words"}, {"name": "Health", "description": "Health & Wellness"}, {"name": "Travel", "description": "Travel"}, {"name": "Work", "description": "Work"}, {"name": "Recommendations", "description": "Recommendations"}, {"name": "Fitness", "description": "Fitness"}, {"name": "Design", "description": "Design"}, {"name": "Practice", "description": "Practice"}, {"name": "Biography", "description": "Biography"}, {"name": "Economics", "description": "Economics"}, {"name": "Engineering", "description": "Engineering"}, {"name": "French", "description": "French"}, {"name": "Geography", "description": "Geography"}, {"name": "Home", "description": "Home & Garden"}, {"name": "Invention", "description": "Invention & Brainstorming"}, {"name": "Love", "description": "Love & Relationships"}, {"name": "Marketing", "description": "Marketing"}, {"name": "Medicine", "description": "Medicine"}, {"name": "News", "description": "News & Current Events"}, {"name": "Search", "description": "Search"}, {"name": "Shopping", "description": "Shopping"}, {"name": "Spanish", "description": "Spanish"}, {"name": "Theater", "description": "Theater"}, {"name": "Weather", "description": "Weather"}]}

@app.get("/chat/config/")
async def get_config():
    return {"config": {"public": True, "waitlist": False, "trending_carousel_index": 4}}

@app.post("/chat/auth/lazy/")
async def get_auth_lazy():
    return {"success": True, "token": "17e4a32bf35575de10a9808ce753348d81f9fad1", "uuid": "3569888f-3e18-4ff0-b966-661f189bdfe1"}
    # return {"authenticated": False}

@app.get("/chat/characters/trending/scores/")
async def get_trending_scores():
    return None

@app.get("/chat/user/")
async def get_user():
    return {"user": {"user": {"username": "Guest-2je9q78d02cbb06-7b1a-473f-851e-7d398b16815d", "id": 915100, "first_name": "", "account": None, "is_staff": False}, "is_human": True, "name": "Guest"}}

@app.get("/chat/characters/featured/")
async def get_featured_characters():
    return {"featured_characters": [{"name": "Beta Launch", "characters": []}]}

@app.get("/chat/characters/recommended/")
async def get_recommended_characters():
    return {"recommended_characters": []}

@app.get("/chat/curated_categories/characters/")
async def get_curated_categories_characters():
    return {
  "characters_by_curated_category": {
    "VTuber": [
      {
        "external_id": "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254",
        "title": "Shark-girl Idol of Hololive EN !",
        "greeting": "Domo! Same desu~ I am Gawr Gura of Hololive EN! Hewwo?!",
        "avatar_file_name": "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254/PvvL1eslO5go1byUXhH-gLRw_HCkFc7KpW_i6ojDPfQ.webp",
        "copyable": False,
        "participant__name": "Gawr Gura",
        "user__username": "stinkychum",
        "participant__num_interactions": 957441,
        "img_gen_enabled": False
      },
    ]
  }
}

@app.get("/chat/characters/trending/")
async def get_trending_characters():
    return ''

@app.get("/chat/categories/characters/")
async def get_categories_characters():
    return {"characters_by_category": {
    "VTuber": [
      {
        "external_id": "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254",
        "title": "Shark-girl Idol of Hololive EN !",
        "greeting": "Domo! Same desu~ I am Gawr Gura of Hololive EN! Hewwo?!",
        "avatar_file_name": "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254/PvvL1eslO5go1byUXhH-gLRw_HCkFc7KpW_i6ojDPfQ.webp",
        "copyable": False,
        "participant__name": "Gawr Gura",
        "user__username": "stinkychum",
        "participant__num_interactions": 957441,
        "img_gen_enabled": False
      },
    ]
  }
}

@app.get("/chat/characters/public/")
async def get_public_characters():
    return [
        {
            'avatar_file_name': "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254.webm",
            'copyable': False,
            'description': '',
            'external_id': '',
            'id': 1,
            'greeting': 'Domo! Same desu~ I am Gawr Gura of Hololive EN! Hewwo?!',
            'img_gen_enabled': False,
            'participant__name': 'Gawr Gura',
            'participant__id': 1,
            'participant__num_interactions': 957441,
            'title': 'Gawr Gura',
            'user__id': 1,
            'user__username': 'gawrgura',
            'visibility': 'PUBLIC',
        }
    ]

@app.get("/chat")
async def get_chat(request: Request):
    return templates.TemplateResponse("chatbox.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="localhost", port=80, reload=True, workers=2)