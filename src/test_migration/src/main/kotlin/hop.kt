import kotlin.math.*

const val BOLTZMANN_CONSTANT = 1.38e-23  // 1.38 * 10^-23 J/K
const val SURFACE_TEMPERATURE = 1.381e2  // 138.1 K
const val TERMINATOR_MERCURY = 3.785e2  // 378.5 K
const val N = 3.7e-1  // Run Parameter as denoted in Butler '97
const val WATER_MASS = 2.989e-26  // 18.02 amu
const val CARBON_DIOXIDE_MASS = 7.308e-26  // 44.01 amu

fun moleculeTemperature(phi: Double): Double {
    // Derive the temperature of a molecule based on latitude
    val moleTemp = (SURFACE_TEMPERATURE + TERMINATOR_MERCURY * cos(phi - (PI / 2)) .pow(N))
    return moleTemp
}

fun launchVelocity(temperature: Double, volatile: Int): Double {
    // Calculate the velocity of the molecule depending on the type
    return if (volatile == 0) {
        sqrt(3 * BOLTZMANN_CONSTANT * temperature / WATER_MASS)
    } else {
        sqrt(3 * BOLTZMANN_CONSTANT * temperature / CARBON_DIOXIDE_MASS)
    }
}

fun calcVelocity(latitude: Double, molecule: Int): Double {
    // Return the velocity of the given molecule
    val temp = moleculeTemperature(latitude)
    val vel = launchVelocity(temp, molecule)
    return vel
}

fun main() {
    var latitude = 1.0 // Test a water molecule at a latitude 1 radian away from the North pole
    var moleculeType = 0
    val val1 = calcVelocity(latitude, moleculeType)
    val test1 = abs(val1 - 826.5) < 0.5
    println("Unit test 1 was $test1")

    latitude = 1.0 // Test a CO2 molecule at a latitude 1 radian away from the North pole
    moleculeType = 1
    val val2 = calcVelocity(latitude, moleculeType)
    val test2 = abs(val2 - 529) < 0.5
    println("Unit test 2 was $test2")

    latitude = PI // Test a CO2 molecule at the South Pole
    moleculeType = -1
    val val3 = calcVelocity(latitude, moleculeType)
    val test3 = abs(val3 - 280) < 0.5
    println("Unit test 3 was $test3")

    latitude = PI/2 // Test a water molecule at the equator
    moleculeType = 0
    val val4 = calcVelocity(latitude, moleculeType)
    val test4 = abs(val4 - 846) < 0.5
    println("Unit test 4 was $test4")

    latitude = 2.0
    moleculeType = 0
    val val5 = calcVelocity(latitude, moleculeType)
    val test5 = abs(val5 - 835) < 0.5
    println("Unit test 5 was $test5")
}