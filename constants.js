sun_r = 696342.0;
jupiter_r = 69911.0;
saturn_r = 58232.0;
uranus_r = 25362.0;
neptune_r = 24622.0;
earth_r = 6371.0;
venus_r = 6051.8;
mars_r = 3389.5;
mercury_r = 2439.7;
saturn_rings_r = 136775;

au =  149597870.7; // km

j2000 = (new Date(2000, 1, 1, 11, 58, 55, 816)).getTime();


// unix timestamp to julian millienium
function jd_for(t) {
  return (t - j2000) / 1000.0 / 3600.0 / 24.0 / 365.25 / 1000.0;
  //return (jd-2451545.0)/365250.0;
}
