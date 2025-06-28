from fastapi import FastAPI
from sqlalchemy.orm.sync import update
from database import SessionDep
from models import Category
from schema import CategoryForm
app = FastAPI()

@app.post("/category")
async def category_create(category: CategoryForm, session: SessionDep):
    new_category = Category(**dict(category))
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return dict(new_category)


@app.patch('/update/category/{id}')
async def category_update(id: int, session: SessionDep, form: CategoryForm):
    employee = await session.get(Category, id)
    await update(form, employee)
    await session.commit()
    await session.refresh(employee)
    return employee

@app.get("/category/{id}",response_model=CategoryForm)
async def category_get(id: int, session: SessionDep):
    employee = await session.get(Category, id)
    return dict(employee)


@app.delete("/category")
async def category_delete(category_id: int, session: SessionDep):
    category = await session.get(Category, category_id)
    category_name = category.name
    await session.delete(category)
    await session.commit()
    return {"message": f"Category {category_name} deleted"}

# echo "# Fars_Api_Basic" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/ArtyomBW/Fars_Api_Basic.git
# git push -u origin main








