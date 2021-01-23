from .models import ParcelList,DriverList


def decide_compartment(parcel_postcode):
    try:
        # Sort parcel based on postcode, postcode should be in range [min_postcode,max_postcode], 
        compartment = DriverList.objects.filter(min_postcode__lte=parcel_postcode).filter(max_postcode__gte=parcel_postcode).values_list('compartment', flat=True)
        destination = DriverList.objects.filter(min_postcode__lte=parcel_postcode).filter(max_postcode__gte=parcel_postcode).values_list('zone', flat=True)

        compartment = int(compartment[0])
        destination = str(destination[0])

    except:
        # if parcel postcode not within any range of pick up point postcode, compartment = 0
        compartment = 0
        destination = str("OTHERS")

    return compartment,destination
