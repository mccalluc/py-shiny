from conftest import create_doc_example_core_fixture
from playwright.sync_api import Page, expect

from shiny.playwright import controller
from shiny.run import ShinyAppProc

app = create_doc_example_core_fixture("input_checkbox_group")


def test_input_checkbox_group_kitchen(page: Page, app: ShinyAppProc) -> None:
    page.goto(app.url)

    colors = controller.InputCheckboxGroup(page, "colors")

    expect(colors.loc_label).to_have_text("Choose color(s):")
    colors.expect_label("Choose color(s):")

    colors.expect_choices(["red", "green", "blue"])
    colors.expect_choice_labels(["Red", "Green", "Blue"])
    colors.expect_selected([])
    colors.expect_inline(False)

    colors.expect_width(None)

    colors.set(["red", "blue"])

    colors.expect_choices(["red", "green", "blue"])
    colors.expect_choice_labels(["Red", "Green", "Blue"])
    colors.expect_selected(["red", "blue"])
