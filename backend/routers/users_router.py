from fastapi import APIRouter, HTTPException, status
import requests

router = APIRouter()


# @router.get("/events/", status_code=200)
# def get_events_by_input():
#     try:
#         tag_list = parse_str_tags_to_list(tags)
#         validate_category(category)
#         raw_events = db_manager.get_events_by(category, tag_list)
#         events = {"events": [Event(event) for event in raw_events]}
#         return events

#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Exeception occured:{}".format(e)
#         )
