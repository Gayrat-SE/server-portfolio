// ############   typing  ##############

var typed = new Typed(".typing", {
    strings: [ "Web Developer","Web Designer", "Youtuber"],
    typeSpeed: 100,
    BacksSpeed: 60,
    loop: true,
})

// ###### aside #####

const nav = document.querySelector(".nav"),
      navList = document.querySelectorAll("li"),
      totalNavList = navList.length,
      allSection = document.querySelectorAll(".section"),
      totalAllSection = allSection.length;
      for(let i =0; i<totalNavList; i++)
      {
          const a = navList[i].querySelector("a");
          a.addEventListener("click", function()
          {
            for(let i=0; i<totalAllSection; i++){
                allSection[i].classList.remove("back-section");
            }
                for (let j = 0; j<totalNavList; j++)
                {
                    if(navList[j].querySelector("a").classList.contains("active"))
                    {
                        allSection[j].classList.add("back-section");
                    }
                    navList[j].querySelector("a").classList.remove("active");
                }
                this.classList.add("active");
                showSelection(this);
                if(window.innerHeight<1200){
                    asideSectionTogglerBtn();
                }
          })
      }
      function showSelection(element){
          for(let i=0; i<totalAllSection; i++){
              allSection[i].classList.remove("active");
          }
          const target = element.getAttribute("href").split("#")[1];
          document.querySelector("#"+target).classList.add("active");
      }
      function updateNav(element){
          for(let i=0; i<totalNavList; i++){
              navList[i].querySelector("a").classList.remove("active");
              const target = element.getAttribute("href").split("#")[1];
              if(target == navList[i].querySelector("a").getAttribute("href").split("#")[1]){
                  navList[i].querySelector("a").classList.add("active");
              }
            }
      }

      document.querySelector(".hire-me").addEventListener("click", function()
          {
            showSelection(this)
            updateNav(this)
          })
      const navToggleBtn = document.querySelector(".nav-toggler"),
            aside = document.querySelector(".aside");
            navToggleBtn.addEventListener("click", () => {
                asideSectionTogglerBtn()
            })
            function asideSectionTogglerBtn(){
                aside.classList.toggle("open");
                navToggleBtn.classList.toggle("open");
                for(let i=0; i<totalAllSection; i++)
                {
                    allSection[i].classList.toggle("open"); 
                }
            }
