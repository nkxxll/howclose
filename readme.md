# Howclose

A python program that calculates how close you where from the latest bad nature event in the world.
With the help of `https://earthquake.usgs.gov` API. It also shows you some information that is
useful or interesting to see.

## API Notes

So the `https://earthquake.usgs.gov/` API endpoint provides me with the option to query for specific
parameters those parameters are explained
[here](https://earthquake.usgs.gov/fdsnws/event/1/#parameters). For the first iteration of this
project I will use a query that checks earthquakes for a specific time frame (1-3 day from the
current date) and filter for events that have a magnitude over 6 this means a noticeable earthquake
that had impact. Then I will take the coordinates of all the events that occurred in the time frame
and calculate the closest event. Some information of this event will then be displayed in the
terminal.

## Development

Install the requirements:

```bash
pip install -r requirements
```

...and then run with...

```bash
python3 .
```

```python
# or with the library
import howclose

hc = howclose.HowClose().full_information()
print(hc)
```

## Feature TODOs

- [ ] add the name of the event to the output
- [ ] name of the city in which the event occurred
- [ ] option to define the lat, lng and a radius if you don't want to use the current position

## Contribute

I’m excited to welcome contributions to **howclose**! If you'd like to contribute, follow the guidelines below to ensure a smooth collaboration:

1. **Fork the Repository:** Start by forking this repository and cloning it to your local
   environment.
2. **Create a Branch:** Work on a separate branch named according to the feature or bugfix you're
   working on, e.g., `feature/cool-new-feature` or `fix/bug-123`.
3. **Code Style:** Consistent code style is important. Ensure your code follows PEP 8 guidelines. I
   recommend using `ruff` for automatic formatting and linting. Before submitting your PR, run the
   formatter:

   ```bash
   ruff .
   ```

4. **Testing:** Make sure that your contribution includes unit tests to verify the new functionality
   or bugfix. Use `pytest` to run the test suite and ensure everything works:

   ```bash
   pytest
   ```

5. **Submit a Pull Request:** Once your branch is ready, push it to your fork and open a PR against
   the `main` branch. Provide a clear explanation of the changes and reference any related issues.
6. **Code Review:** Your PR will be reviewed, and you might receive feedback or requested changes to
   ensure the code meets the project’s standards.

Thank you for contributing to **howclose**!
