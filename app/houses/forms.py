from django import forms


class HouseFilterForms(forms.Form):
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(
        label="сортировка",
        required=False,
        choices=[
            ["name", "по алфавиту"],
            ["-name", "по алфавиту обратно"],
            ["price", "по цене >>"],
            ["-price", "по цене <<"],
        ],
    )
