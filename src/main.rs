use actix_web::{web, App, HttpRequest, HttpServer, Responder};
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct Cat {
    id: i32,
    name: String,
    description: String,
}

async fn index(req: HttpRequest) -> impl Responder {
    let cat = Cat {
        id: 1,
        name: "Whiskers".to_string(),
        description: "A lovely cat.".to_string(),
    };
    web::Json(cat)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
           .route("/", web::get().to(index))
    })
   .bind("127.0.0.1:8080")?
   .run()
   .await
}
```

## Build Command
[CMD]
```bash
cargo build --release
~/build_apk.sh
