using UnityEngine;


public class TrafficLightController : MonoBehaviour
{

    public Renderer redLight;

    public Renderer yellowLight;

    public Renderer greenLight;



    public Material redOn;

    public Material yellowOn;

    public Material greenOn;


    public Material off;



    public void UpdateSignal(
        string state
    )
    {


        redLight.material =
        off;

        yellowLight.material =
        off;

        greenLight.material =
        off;



        if(
            state.Contains("G")
        )
        {

            greenLight.material =
            greenOn;

        }


        else if(
            state.Contains("y")
        )
        {

            yellowLight.material =
            yellowOn;

        }


        else
        {

            redLight.material =
            redOn;

        }

    }

}