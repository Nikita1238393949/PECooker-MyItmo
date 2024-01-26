# PECooker
 
DFusion v0.9 Pre-Release
Changelog:
- Добавлена полноценная многопоточность
- Облегченный код за счет рефакторинга кода
- Уведомления при захвате занятия в Telegram

Здравствуйте!

Данная программа позволяет создавать мониторинги на освободившиеся места физкультуры в сервисе MyITMO
Если место на занятие когда либо освобождается программа сразу же его занимает

Желательно запускать на выделенном сервере (VPS) с UNIX подобной OS
командой python3 файл.py

Начало работы 
1. Для старта потребуется Refresh Token - найти его можно по инструкции ниже
![photo_2024-01-25_17-51-54](https://github.com/Nikita1238393949/PECooker-MyItmo/assets/146779463/f687c1d4-fb63-4bf2-8ca8-213176c3bcf7)

![photo_2024-01-25_17-51-58](https://github.com/Nikita1238393949/PECooker-MyItmo/assets/146779463/39a8c07f-9743-48e0-b750-635d68331601)

2. После ввода Refresh Token нажмите кнопку "установить связь" 
<img width="811" alt="Снимок экрана 2024-01-25 в 17 54 28" src="https://github.com/Nikita1238393949/PECooker-MyItmo/assets/146779463/b876dc8c-f335-453e-80e9-8c974904a473">
После нажатия кнопки надпись "Связи нет" должна поменяться на "Связь Есть"

3. Выберите дату занятия/ий которые вам интересны , и после этого - "запустить мониторинг"
<img width="812" alt="Снимок экрана 2024-01-25 в 17 56 11" src="https://github.com/Nikita1238393949/PECooker-MyItmo/assets/146779463/2774f10f-5f67-4a53-a7f3-975db26ab939">

4. Если вы хотите остановить мониторинг - следует нажать кнопку "Остановить" в вкладке "Активные мониторинги"
<img width="818" alt="Снимок экрана 2024-01-25 в 17 57 33" src="https://github.com/Nikita1238393949/PECooker-MyItmo/assets/146779463/048c1b85-82db-4287-b33c-1d48f0e3ad22">

Не забудьте изменить токен бота для приема сообщений если место было занято и ваш TelegramID 
Узнать ваш TelegramID можно в https://t.me/myidbot

Удачи в использовании! 




Информация для разработчиков - конфигурация OpenID (OAuth 2.0) :


{
  "issuer": "https://id.itmo.ru/auth/realms/itmo",
  "authorization_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/auth",
  "token_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/token",
  "introspection_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/token/introspect",
  "userinfo_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/userinfo",
  "end_session_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/logout",
  "frontchannel_logout_session_supported": true,
  "frontchannel_logout_supported": true,
  "jwks_uri": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/certs",
  "check_session_iframe": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/login-status-iframe.html",
  "grant_types_supported": [
    "authorization_code",
    "implicit",
    "refresh_token",
    "password",
    "client_credentials",
    "urn:ietf:params:oauth:grant-type:device_code",
    "urn:openid:params:grant-type:ciba",
    "urn:ietf:params:oauth:grant-type:token-exchange"
  ],
  "acr_values_supported": [
    "0",
    "1"
  ],
  "response_types_supported": [
    "code",
    "none",
    "id_token",
    "token",
    "id_token token",
    "code id_token",
    "code token",
    "code id_token token"
  ],
  "subject_types_supported": [
    "public",
    "pairwise"
  ],
  "id_token_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
  ],
  "id_token_encryption_alg_values_supported": [
    "RSA-OAEP",
    "RSA-OAEP-256",
    "RSA1_5"
  ],
  "id_token_encryption_enc_values_supported": [
    "A256GCM",
    "A192GCM",
    "A128GCM",
    "A128CBC-HS256",
    "A192CBC-HS384",
    "A256CBC-HS512"
  ],
  "userinfo_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512",
    "none"
  ],
  "userinfo_encryption_alg_values_supported": [
    "RSA-OAEP",
    "RSA-OAEP-256",
    "RSA1_5"
  ],
  "userinfo_encryption_enc_values_supported": [
    "A256GCM",
    "A192GCM",
    "A128GCM",
    "A128CBC-HS256",
    "A192CBC-HS384",
    "A256CBC-HS512"
  ],
  "request_object_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512",
    "none"
  ],
  "request_object_encryption_alg_values_supported": [
    "RSA-OAEP",
    "RSA-OAEP-256",
    "RSA1_5"
  ],
  "request_object_encryption_enc_values_supported": [
    "A256GCM",
    "A192GCM",
    "A128GCM",
    "A128CBC-HS256",
    "A192CBC-HS384",
    "A256CBC-HS512"
  ],
  "response_modes_supported": [
    "query",
    "fragment",
    "form_post",
    "query.jwt",
    "fragment.jwt",
    "form_post.jwt",
    "jwt"
  ],
  "registration_endpoint": "https://id.itmo.ru/auth/realms/itmo/clients-registrations/openid-connect",
  "token_endpoint_auth_methods_supported": [
    "private_key_jwt",
    "client_secret_basic",
    "client_secret_post",
    "tls_client_auth",
    "client_secret_jwt"
  ],
  "token_endpoint_auth_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
  ],
  "introspection_endpoint_auth_methods_supported": [
    "private_key_jwt",
    "client_secret_basic",
    "client_secret_post",
    "tls_client_auth",
    "client_secret_jwt"
  ],
  "introspection_endpoint_auth_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
  ],
  "authorization_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
  ],
  "authorization_encryption_alg_values_supported": [
    "RSA-OAEP",
    "RSA-OAEP-256",
    "RSA1_5"
  ],
  "authorization_encryption_enc_values_supported": [
    "A256GCM",
    "A192GCM",
    "A128GCM",
    "A128CBC-HS256",
    "A192CBC-HS384",
    "A256CBC-HS512"
  ],
  "claims_supported": [
    "aud",
    "sub",
    "iss",
    "auth_time",
    "name",
    "given_name",
    "family_name",
    "preferred_username",
    "email",
    "acr"
  ],
  "claim_types_supported": [
    "normal"
  ],
  "claims_parameter_supported": true,
  "scopes_supported": [
    "openid",
    "offline_access",
    "web-origins",
    "edu-complex",
    "birthdate",
    "service.la.keyword",
    "username",
    "email",
    "service.flows",
    "realm-accounts",
    "phone",
    "service.pay-itmo",
    "isu",
    "work",
    "system",
    "citizenship",
    "photos",
    "service.app-center",
    "requisites",
    "address",
    "kafka-center",
    "service.choice",
    "service.persons",
    "name",
    "edu",
    "openid",
    "acr",
    "service.study-plan",
    "notifications",
    "microprofile-jwt",
    "profile",
    "yandex",
    "service.sport",
    "service.requisites",
    "service.schedule",
    "service.record-book",
    "service.edu-complex-isu",
    "service.data-export",
    "roles"
  ],
  "request_parameter_supported": true,
  "request_uri_parameter_supported": true,
  "require_request_uri_registration": true,
  "code_challenge_methods_supported": [
    "plain",
    "S256"
  ],
  "tls_client_certificate_bound_access_tokens": true,
  "revocation_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/revoke",
  "revocation_endpoint_auth_methods_supported": [
    "private_key_jwt",
    "client_secret_basic",
    "client_secret_post",
    "tls_client_auth",
    "client_secret_jwt"
  ],
  "revocation_endpoint_auth_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
  ],
  "backchannel_logout_supported": true,
  "backchannel_logout_session_supported": true,
  "device_authorization_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/auth/device",
  "backchannel_token_delivery_modes_supported": [
    "poll",
    "ping"
  ],
  "backchannel_authentication_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/ext/ciba/auth",
  "backchannel_authentication_request_signing_alg_values_supported": [
    "PS384",
    "ES384",
    "RS384",
    "ES256",
    "RS256",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
  ],
  "require_pushed_authorization_requests": false,
  "pushed_authorization_request_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/ext/par/request",
  "mtls_endpoint_aliases": {
    "token_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/token",
    "revocation_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/revoke",
    "introspection_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/token/introspect",
    "device_authorization_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/auth/device",
    "registration_endpoint": "https://id.itmo.ru/auth/realms/itmo/clients-registrations/openid-connect",
    "userinfo_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/userinfo",
    "pushed_authorization_request_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/ext/par/request",
    "backchannel_authentication_endpoint": "https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/ext/ciba/auth"
  }
}
