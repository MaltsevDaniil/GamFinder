from users.schemas import CreateUser, User
from users.settings import SessionLocal

def create_user(user_in: CreateUser):
    db = SessionLocal()
    db_user = User(
        id = user_in.id,
        image=user_in.image,
        name=user_in.name,
        age=user_in.age,
        sex=user_in.sex,
        description=user_in.description,
        games=",".join(user_in.games),
        who_likes=",".join(map(str, user_in.who_likes)),
        recomends=",".join(map(str, user_in.recomends))
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

def get_user(id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    if user:
        return { "msg": "ok","user": user }
    return {"msg": "User not found"}

def get_all_users():
    db = SessionLocal()
    return {"msg": "ok",
            "users": db.query(User).all(),
            }

def compute_sym_diff(user_games, other_user_games):
    user_set = set(user_games.split(',')) if user_games else set()
    other_user_set = set(other_user_games.split(',')) if other_user_games else set()
    return len(user_set.symmetric_difference(other_user_set))

def update_recommends(user_id: int):
    db = SessionLocal()
    users = db.query(User).filter(User.id != user_id).all()
    main_user = db.query(User).filter(User.id == user_id).first()
    if main_user.games == "":
        main_user.recomends = ",".join(str(us.id) for us in db.query(User).filter(User.id != user_id).all())
        db.commit()
        db.close()
        return
    sym_diff_list = []
    for other_user in users:
        symdiff = compute_sym_diff(main_user.games, other_user.games)
        sym_diff_list.append((symdiff, other_user.id))

    sym_diff_list.sort(key=lambda x: x[0])
    sorted_user_ids = [str(user_ids) for symdif, user_ids in sym_diff_list]
    main_user.recomends = ",".join(sorted_user_ids)
    db.commit()
    db.close()

def get_recomend_profile(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    recomends = user.recomends
    if recomends:
        comma_index = recomends.find(',')
        if comma_index != -1:
            first_rec_id = recomends[:comma_index]
            new_rec = recomends[comma_index+1:]
            print(new_rec)
        else:
            first_rec_id = recomends
            new_rec = ""
        user.recomends = new_rec
        db.commit()
        db.close()
        return {"msg": "Ok", "rec_user": get_user(int(first_rec_id))}
    else:
        print(user_id)
        update_recommends(user_id)
        return get_recomend_profile(user_id)

def update_image(user_id: int, image: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.image = image
    db.commit()
    db.close()
    return {"msg": "Ok", "message": image}

def update_name(user_id: int, name: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.name = name
    db.commit()
    db.close()
    return {"msg": "Ok", "message": name}

def update_description(user_id: int, description: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.description = description
    db.commit()
    db.close()
    return {"msg": "Ok", "message": description}

def update_age(user_id: int, age: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.age = age
    db.commit()
    db.close()
    return {"msg": "Ok", "message": age}

def update_games(user_id: int, games: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.games = games
    db.commit()
    db.close()
    return {"msg": "Ok", "message": games}