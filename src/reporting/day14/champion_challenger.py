champion_mape = 8.5

challenger_mape = 2.58

improvement = (

    (champion_mape - challenger_mape)

    / champion_mape

) * 100

print(
    "Improvement:",
    round(improvement,2),
    "%"
)

if improvement >= 5:

    print(
        "Promote Challenger"
    )

else:

    print(
        "Keep Champion"
    )