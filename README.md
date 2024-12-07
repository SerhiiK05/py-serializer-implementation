def# Serializer Implementation

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before start.

In this task, you should implement the `CarSerializer` serializer for the `Car` model in `serializers.py`.

The `Car` model has the following fields:
- manufacturer (with the `max_length` of 64);
- model (with the `max_length` of 64);
- horse_powers (with the minimum and maximum validators);
- is_broken;
- problem_description (can be `null`).

Serializer should be created using **serializers.Serializer**.

Also, you should implement 2 functions that use the `CarSerializer` in `main.py`:
- `serialize_car_object`, that accepts the `Car` object and returns `json` with its data;
- `deserialize_car_object`, that accepts `json` and returns the `Car` instance.
