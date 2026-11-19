# HTTP Fundamentals

## 1. Overview & Architecture
* **Client:** Browser or application initiating the request[cite: 3].
* **Server:** HTTP web server handling the request and returning a response[cite: 3].
* **Stateless Protocol:** The server keeps no memory of past interactions[cite: 3]. 
  * *Why it matters:* Simplifies server architecture and improves scalability—requests can be distributed across any server without a single server needing to track session state if one goes down[cite: 3].

### HTTP Versions
* **HTTP/1.1:** Introduced persistent TCP connections (`keep-alive`) to reduce latency[cite: 1, 3].
* **HTTP/2:** Introduced header compression, multiplexing, and stronger default security (HTTPS)[cite: 3].

### OSI Model Context
Data flows down from Layer 7 to Layer 1 when transmitting, and up from Layer 1 to Layer 7 when receiving[cite: 3]:
1. **7. Application Layer** *(HTTP lives here)*[cite: 3]
2. **6. Presentation Layer**[cite: 3]
3. **5. Session Layer**[cite: 3]
4. **4. Transport Layer** *(TCP/UDP)*[cite: 3]
5. **3. Network Layer** *(IP)*[cite: 3]
6. **2. Data Link Layer**[cite: 3]
7. **1. Physical Layer**[cite: 3]

---

## 2. Request & Response Structure

**HTTP Request:**
* **URL** (Endpoint)[cite: 3]
* **Method Type** (`GET`, `POST`, etc.)[cite: 2, 3]
* **Headers**[cite: 3]
* **Body** *(optional)*[cite: 3]

**HTTP Response:**
* **Status Code**[cite: 3]
* **Headers**[cite: 3]
* **Body** *(optional)*[cite: 3]

---

## 3. HTTP Headers
HTTP is extensible because custom headers can be added without breaking the underlying protocol[cite: 2].

### Request Headers (Client $\rightarrow$ Server)
Provide metadata about the client and the request[cite: 3]:
* `User-Agent`: Identifies the client type (browser, OS, mobile app)[cite: 3].
* `Authorization`: Carries credentials/tokens to authenticate the user[cite: 3].
* `Cookie`: Sends stored cookies back to the server[cite: 3].
* `Accept`: Specifies the media/content types the client can accept[cite: 3].

### General Headers
Apply to both requests and responses[cite: 3]:
* `Date`: Timestamp of when the message was generated[cite: 3].
* `Cache-Control`: Directives for caching mechanisms[cite: 3].
* `Connection`: Controls whether the network connection stays open (e.g., `keep-alive`)[cite: 1, 3].

### Representation Headers
Describe the payload/body format[cite: 2]:
* `Content-Type`: Media type of the resource (e.g., `application/json`)[cite: 2].
* `Content-Length`: Size of the body in bytes[cite: 2].
* `Content-Encoding`: Compression algorithm used (e.g., `gzip`)[cite: 2].
* `ETag`: Unique identifier for a specific version of a resource (used for caching)[cite: 2].

### Security Headers
* `Strict-Transport-Security` (**HSTS**): Enforces HTTPS connections[cite: 2].
* `Content-Security-Policy` (**CSP**): Prevents XSS and data injection attacks[cite: 2].
* `X-Frame-Options`: Protects against clickjacking by controlling iframe embedding[cite: 2].
* `X-Content-Type-Options`: Prevents MIME-type sniffing[cite: 2].
* `Set-Cookie`: Sends cookies from the server to the client securely[cite: 2].

---

## 4. HTTP Methods

| Method | Purpose | Idempotent? |
| :--- | :--- | :--- |
| **`GET`** | Fetch data from the server without modifying it[cite: 2]. | Yes[cite: 2] |
| **`POST`** | Submit/create new data on the server[cite: 2]. | No[cite: 2] |
| **`PUT`** | Replace an existing resource entirely[cite: 2]. | Yes[cite: 2] |
| **`PATCH`** | Partially update an existing resource[cite: 2]. | No *(usually)* |
| **`DELETE`** | Remove a resource from the server[cite: 2]. | Yes[cite: 2] |
| **`HEAD`** | Same as `GET`, but returns only response headers (no body)[cite: 1]. | Yes |
| **`OPTIONS`** | Describe communication options/capabilities of the target server[cite: 2]. | Yes |

> **Idempotency:** An operation is *idempotent* if making the same request multiple times produces the exact same state/result on the server as making it once[cite: 2].

---

## 5. CORS & Preflighted Requests
* **CORS (Cross-Origin Resource Sharing):** A browser security mechanism that controls how web applications interact with resources hosted on different domains[cite: 2].
* **Preflight Request:** An automatic `OPTIONS` request sent by the browser before the actual request to check if the server permits it[cite: 1, 2]. A preflight is triggered if:
  1. The request uses non-simple headers (e.g., `Authorization`, `X-Custom-Header`)[cite: 2].
  2. The `Content-Type` is anything other than `application/x-www-form-urlencoded`, `multipart/form-data`, or `text/plain`[cite: 1, 2].
  3. The HTTP method is not `GET`, `HEAD`, or `POST` (e.g., it uses `PUT`, `DELETE`, or `PATCH`)[cite: 1].

---

## 6. HTTP Status Codes

* **`1xx` — Informational:** Request received, continuing process[cite: 1].
* **`2xx` — Success:**
  * `200 OK`: Standard success response[cite: 1].
  * `201 Created`: New resource successfully created[cite: 1].
  * `204 No Content`: Request succeeded, no body returned[cite: 1].
* **`3xx` — Redirection:**
  * `301 Moved Permanently`: Resource permanently moved to a new URL[cite: 1].
  * `302 Found`: Resource temporarily moved[cite: 1].
  * `304 Not Modified`: Cached version is still valid; no need to re-download[cite: 1].
* **`4xx` — Client Error:**
  * `400 Bad Request`: Malformed syntax or invalid request parameters[cite: 1].
  * `401 Unauthorized`: Authentication is required or has failed[cite: 1].
  * `403 Forbidden`: Client is authenticated, but lacks permission to access the resource[cite: 1].
* **`5xx` — Server Error:**
  * `500 Internal Server Error`: Generic unexpected server-side failure[cite: 1].

---

## 7. Performance & Communication Mechanisms
* **HTTP Caching:** Storing copies of responses for reuse to reduce latency and server load[cite: 1].
* **Content Negotiation:** Mechanism where the client and server agree on the best format to exchange data (using preferred and fallback formats via headers like `Accept`)[cite: 1].
* **Keep-Alive:** Allows the client and server to reuse the same TCP connection for multiple requests/responses instead of opening a new one each time[cite: 1].
* **Remote Control:** Allows the client to send instructions or preferences on how content is handled/served[cite: 2].