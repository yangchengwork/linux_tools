package temperature

type Temperature float64

func CtoF(c float64) Temperature {
	return Temperature((c * (9.0 / 5.0)) + 32)
}

func FtoC(f float64) Temperature {
	return Temperature((f - 32) * (5.0 / 9.0))
}
