using System.Collections.Generic;
using System.IO;
using UnityEngine;


// ===============================
// DATA STRUCTURES
// ===============================


[System.Serializable]
public class CarData
{
    public string id;

    public float x;

    public float y;

    public float angle;

    public float speed;
}



[System.Serializable]
public class TrafficLightData
{
    public string id;

    public string state;
}



[System.Serializable]
public class TrafficPacket
{
    public List<CarData> cars;

    public TrafficLightData traffic_light;
}



// ===============================
// TRAFFIC MANAGER
// ===============================


public class TrafficManager : MonoBehaviour
{

    public GameObject carPrefab;
    public TrafficLightController northLight;

    public TrafficLightController southLight;

    public TrafficLightController eastLight;

    public TrafficLightController westLight;



    Dictionary<string, GameObject> vehicles
    =
    new Dictionary<string, GameObject>();



    string jsonPath;



    float updateTimer = 0;



    // SUMO to Unity scale

    float scale = 1f;



    void Start()
    {

        jsonPath =
        Application.dataPath
        +
        "/../../traffic_data.json";



        Debug.Log(
            "Reading JSON: "
            +
            jsonPath
        );

    }



    void Update()
    {


        // only update 10 FPS

        updateTimer += Time.deltaTime;


        if(updateTimer < 0.1f)
            return;


        updateTimer = 0;



        // check file


        if(
            !File.Exists(jsonPath)
        )
        {

            Debug.Log(
                "JSON not found"
            );

            return;

        }



        string json;



        try
        {

            json =
            File.ReadAllText(
                jsonPath
            );

        }


        catch
        {

            return;

        }




        TrafficPacket packet =
        JsonUtility
        .FromJson<TrafficPacket>(
            json
        );



        if(
            packet == null
            ||
            packet.cars == null
        )
        {

            return;

        }




        Debug.Log(
            "Cars received: "
            +
            packet.cars.Count
        );

        Debug.Log(
            "Signal State: "
            +
            packet.traffic_light.state
        );

        string signal =
        packet.traffic_light.state;


        if(signal.Length >= 12)
        {

            Debug.Log(
                "Updating traffic lights"
                );

             northLight.UpdateSignal(
                signal[0].ToString()
            );


             eastLight.UpdateSignal(
                signal[3].ToString()
            );  


            southLight.UpdateSignal(
                signal[6].ToString()
            );


            westLight.UpdateSignal(
                signal[9].ToString()
            );

        }



        HashSet<string> activeCars =
        new HashSet<string>();



        foreach(
            CarData car
            in packet.cars
        )
        {


            activeCars.Add(
                car.id
            );



            Vector3 position =
            new Vector3(

                car.x,

                0.4f,

                car.y

            );



            Quaternion rotation =
            Quaternion.Euler(

                0,

                car.angle - 90,

                0

            );




            // Spawn new car

            if(
                !vehicles
                .ContainsKey(
                    car.id
                )
            )

            {

                GameObject obj =
                Instantiate(

                    carPrefab,

                    position,

                    rotation

                );



                obj.name =
                car.id;



                vehicles.Add(

                    car.id,

                    obj

                );

            }



            // Move existing car

            else

            {


                GameObject obj =
                vehicles[
                    car.id
                ];



                obj
                .transform
                .position
                =
                Vector3.Lerp(

                    obj.transform.position,

                    position,

                    Time.deltaTime * 5

                );



                obj
                .transform
                .rotation
                =
                Quaternion.Lerp(

                    obj.transform.rotation,

                    rotation,

                    Time.deltaTime * 5

                );


            }


        }




        // Remove cars that left SUMO


        List<string> remove =
        new List<string>();


        foreach(
            string id
            in vehicles.Keys
        )

        {

            if(
                !activeCars
                .Contains(id)
            )

            {

                remove.Add(
                    id
                );

            }

        }




        foreach(
            string id
            in remove
        )

        {

            Destroy(
                vehicles[id]
            );


            vehicles.Remove(
                id
            );

        }



    }


}