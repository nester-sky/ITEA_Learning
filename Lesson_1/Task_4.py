# 4) Реализовать функцию bank, которая приннимает следующие
# аргументы: сумма депозита, кол-во лет, и процент. Результатом
# выполнения должна быть сумма по истечению депозита


def bank(deposit, years, percent):
    for i in range(0, years):
        deposit += deposit * percent / 100
    return deposit


final_sum_deposit = bank(10000, 2, 10)
print(final_sum_deposit)
