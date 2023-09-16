#!/usr/bin/python3
'''
Module that defines a new view for Review objects
that handles all default RESTFul API actions.
'''
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User
from api.v1.views import app_views


@app_views.route(
    '/places/<place_id>/reviews',
    methods=['GET'],
    strict_slashes=False
)
def get_reviews_of_place(place_id):
    '''
    Retrieves the list of all Review objects of a Place
    '''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(
        [review.to_dict() for review in place.reviews]
    )


@app_views.route(
    '/reviews/<review_id>',
    methods=['GET'],
    strict_slashes=False
)
def get_review(review_id):
    '''
    Retrieves a Review object based on review_id
    '''
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route(
    '/reviews/<review_id>',
    methods=['DELETE'],
    strict_slashes=False
)
def delete_review(review_id):
    '''
    Deletes a Review object based on review_id
    '''
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route(
    '/places/<place_id>/reviews',
    methods=['POST'],
    strict_slashes=False
)
def create_review(place_id):
    '''
    Creates a Review for a Place
    '''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    if 'text' not in data:
        abort(400, 'Missing text')
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    data['place_id'] = place_id
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route(
    '/reviews/<review_id>',
    methods=['PUT'],
    strict_slashes=False
)
def update_review(review_id):
    '''
    Updates a Review object based on review_id
    '''
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in [
            'id',
            'user_id',
            'place_id',
            'created_at',
            'updated_at'
        ]:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
