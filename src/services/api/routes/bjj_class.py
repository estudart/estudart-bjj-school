import logging

from flask import Blueprint

from services.api.controllers.bjj_class import (
    get_class_by_id,
    post_class,
    delete_class_by_id
)



bp_class = Blueprint("class",
                     __name__)