using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SlideController : MonoBehaviour
{
    public Material Page1;
    public Material Page2;
    int c = 0;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        if (Input.GetButtonDown("Fire1"))
        {
            if(c == 0)
                this.GetComponent<MeshRenderer> ().material = Page1;
            else if(c == 1)
                this.GetComponent<MeshRenderer> ().material = Page2;
            c = c + 1;
            c = c % 2;
            // Debug.Log(c);
        }
    }
}
