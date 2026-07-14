using UnityEngine;
using System.IO;

public class CCTVCapture : MonoBehaviour
{
    public string cameraName;

    private Camera cam;

    private RenderTexture renderTexture;
    private Texture2D captureTexture;

    private float timer = 0f;

    private string savePath;

    void Start()
    {
        cam = GetComponent<Camera>();

        // Allocate ONCE
        renderTexture = new RenderTexture(1280, 720, 24);
        captureTexture = new Texture2D(
            1280,
            720,
            TextureFormat.RGB24,
            false
        );

        savePath =
            Application.dataPath +
            "/../../../camera_feed/" +
            cameraName +
            ".jpg";

        Debug.Log($"{cameraName} camera initialized.");
    }

    void Update()
    {
        timer += Time.deltaTime;

        // 5 FPS
        if (timer < 0.2f)
            return;

        timer = 0f;

        cam.targetTexture = renderTexture;
        cam.Render();

        RenderTexture.active = renderTexture;

        captureTexture.ReadPixels(
            new Rect(0, 0, 1280, 720),
            0,
            0
        );

        captureTexture.Apply();

        File.WriteAllBytes(
            savePath,
            captureTexture.EncodeToJPG(85)
        );

        cam.targetTexture = null;
        RenderTexture.active = null;
    }

    void OnDestroy()
    {
        if (renderTexture != null)
        {
            renderTexture.Release();
            Destroy(renderTexture);
        }

        if (captureTexture != null)
        {
            Destroy(captureTexture);
        }
    }
}