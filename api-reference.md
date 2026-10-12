# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [SpotifyWebApiClient](spotify_web_api/client.py)

## Albums

> Source: [Albums](spotify_web_api/apis/albums.py)

<details>
<summary><code>def check_users_saved_albums(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.check_users_saved_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.check_users_saved_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedAlbumsErrorBody](spotify_web_api/errors/check_users_saved_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_album(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AlbumObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single album.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.get_an_album("4aawyAB9vmqN3uQ7FjRGTy", market="ES")
    # TODO: Handle 'response' of type AlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAlbumErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.get_an_album("4aawyAB9vmqN3uQ7FjRGTy", market="ES")
    # TODO: Handle 'response' of type AlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAlbumErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AlbumObject](spotify_web_api/models/album_object.py)</code> -- An album

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnAlbumErrorBody](spotify_web_api/errors/get_an_album_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_albums_tracks(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSimplifiedTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an album’s tracks.
Optional parameters can be used to limit the number of tracks returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.get_an_albums_tracks("4aawyAB9vmqN3uQ7FjRGTy", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAlbumsTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.get_an_albums_tracks("4aawyAB9vmqN3uQ7FjRGTy", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAlbumsTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSimplifiedTrackObject](spotify_web_api/models/paging_simplified_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnAlbumsTracksErrorBody](spotify_web_api/errors/get_an_albums_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_artists_albums(id_: str, *, include_groups: str | None = None, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingArtistDiscographyAlbumObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an artist's albums.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.get_an_artists_albums(
        "0TnOYISbd1XYRBk9myaseg", include_groups="single,appears_on", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingArtistDiscographyAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.get_an_artists_albums(
        "0TnOYISbd1XYRBk9myaseg", include_groups="single,appears_on", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingArtistDiscographyAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>include_groups</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingArtistDiscographyAlbumObject](spotify_web_api/models/paging_artist_discography_album_object.py)</code> -- Pages of albums

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnArtistsAlbumsErrorBody](spotify_web_api/errors/get_an_artists_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multiple_albums(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyAlbums</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for multiple albums identified by their Spotify IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.get_multiple_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc", market="ES"
    )
    # TODO: Handle 'response' of type ManyAlbums
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.get_multiple_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc", market="ES"
    )
    # TODO: Handle 'response' of type ManyAlbums
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyAlbums](spotify_web_api/models/many_albums.py)</code> -- A set of albums

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetMultipleAlbumsErrorBody](spotify_web_api/errors/get_multiple_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_new_releases(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagedAlbums</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.get_new_releases(limit=10, offset=5)
    # TODO: Handle 'response' of type PagedAlbums
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNewReleasesErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.get_new_releases(limit=10, offset=5)
    # TODO: Handle 'response' of type PagedAlbums
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNewReleasesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagedAlbums](spotify_web_api/models/paged_albums.py)</code> -- A paged set of albums

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetNewReleasesErrorBody](spotify_web_api/errors/get_new_releases_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_albums(*, limit: int | None = 20, offset: int | None = 0, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PagingSavedAlbumObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the albums saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.albums.get_users_saved_albums(limit=10, offset=5, market="ES")
    # TODO: Handle 'response' of type PagingSavedAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.albums.get_users_saved_albums(limit=10, offset=5, market="ES")
    # TODO: Handle 'response' of type PagingSavedAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedAlbumObject](spotify_web_api/models/paging_saved_album_object.py)</code> -- Pages of albums

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedAlbumsErrorBody](spotify_web_api/errors/get_users_saved_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_albums_user(ids: str, *, body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more albums from the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.albums.remove_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAlbumsUserErrorBody
```

**Async**

```python
try:
    await async_client.albums.remove_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAlbumsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RemoveAlbumsRequest](spotify_web_api/models/remove_albums_request.py) \| [RemoveAlbumsRequestDict](spotify_web_api/models/remove_albums_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveAlbumsUserErrorBody](spotify_web_api/errors/remove_albums_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_albums_user(ids: str, *, body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more albums to the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.albums.save_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAlbumsUserErrorBody
```

**Async**

```python
try:
    await async_client.albums.save_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAlbumsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveAlbumsRequest](spotify_web_api/models/save_albums_request.py) \| [SaveAlbumsRequestDict](spotify_web_api/models/save_albums_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveAlbumsUserErrorBody](spotify_web_api/errors/save_albums_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Artists

> Source: [Artists](spotify_web_api/apis/artists.py)

<details>
<summary><code>def check_current_user_follows(type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check to see if the current user is following one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.check_current_user_follows(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCurrentUserFollowsErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.check_current_user_follows(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCurrentUserFollowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType3OrStr](spotify_web_api/models/enums/item_type3.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckCurrentUserFollowsErrorBody](spotify_web_api/errors/check_current_user_follows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def follow_artists_users(type_: ItemType2OrStr, ids: str, *, body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add the current user as a follower of one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.artists.follow_artists_users(
        ItemType2.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowArtistsUsersErrorBody
```

**Async**

```python
try:
    await async_client.artists.follow_artists_users(
        ItemType2.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowArtistsUsersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType2OrStr](spotify_web_api/models/enums/item_type2.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[FollowArtistsOrUsersRequest](spotify_web_api/models/follow_artists_or_users_request.py) \| [FollowArtistsOrUsersRequestDict](spotify_web_api/models/follow_artists_or_users_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[FollowArtistsUsersErrorBody](spotify_web_api/errors/follow_artists_users_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_artist(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> ArtistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single artist identified by their unique Spotify ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_an_artist("0TnOYISbd1XYRBk9myaseg")
    # TODO: Handle 'response' of type ArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_an_artist("0TnOYISbd1XYRBk9myaseg")
    # TODO: Handle 'response' of type ArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ArtistObject](spotify_web_api/models/artist_object.py)</code> -- An artist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnArtistErrorBody](spotify_web_api/errors/get_an_artist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_artists_albums(id_: str, *, include_groups: str | None = None, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingArtistDiscographyAlbumObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an artist's albums.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_an_artists_albums(
        "0TnOYISbd1XYRBk9myaseg", include_groups="single,appears_on", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingArtistDiscographyAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_an_artists_albums(
        "0TnOYISbd1XYRBk9myaseg", include_groups="single,appears_on", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingArtistDiscographyAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>include_groups</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingArtistDiscographyAlbumObject](spotify_web_api/models/paging_artist_discography_album_object.py)</code> -- Pages of albums

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnArtistsAlbumsErrorBody](spotify_web_api/errors/get_an_artists_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_artists_related_artists(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> ManyArtists</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of the Spotify community's listening history.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_an_artists_related_artists("0TnOYISbd1XYRBk9myaseg")
    # TODO: Handle 'response' of type ManyArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsRelatedArtistsErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_an_artists_related_artists("0TnOYISbd1XYRBk9myaseg")
    # TODO: Handle 'response' of type ManyArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsRelatedArtistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyArtists](spotify_web_api/models/many_artists.py)</code> -- A set of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnArtistsRelatedArtistsErrorBody](spotify_web_api/errors/get_an_artists_related_artists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_artists_top_tracks(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyTracks</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an artist's top tracks by country.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_an_artists_top_tracks("0TnOYISbd1XYRBk9myaseg", market="ES")
    # TODO: Handle 'response' of type ManyTracks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsTopTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_an_artists_top_tracks("0TnOYISbd1XYRBk9myaseg", market="ES")
    # TODO: Handle 'response' of type ManyTracks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsTopTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyTracks](spotify_web_api/models/many_tracks.py)</code> -- A set of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnArtistsTopTracksErrorBody](spotify_web_api/errors/get_an_artists_top_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_followed(type_: ItemType1OrStr, *, after: str | None = None, limit: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> CursorPagedArtists</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's followed artists.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_followed(ItemType1.ARTIST, after="0I2XqVXqHScXjHhk6AYYRe", limit=10)
    # TODO: Handle 'response' of type CursorPagedArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFollowedErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_followed(ItemType1.ARTIST, after="0I2XqVXqHScXjHhk6AYYRe", limit=10)
    # TODO: Handle 'response' of type CursorPagedArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFollowedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType1OrStr](spotify_web_api/models/enums/item_type1.py)</code> | Value sent with the request. |
| <code>after</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CursorPagedArtists](spotify_web_api/models/cursor_paged_artists.py)</code> -- A paged set of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetFollowedErrorBody](spotify_web_api/errors/get_followed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multiple_artists(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> ManyArtists</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for several artists based on their Spotify IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_multiple_artists(
        "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type ManyArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleArtistsErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_multiple_artists(
        "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type ManyArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleArtistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyArtists](spotify_web_api/models/many_artists.py)</code> -- A set of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetMultipleArtistsErrorBody](spotify_web_api/errors/get_multiple_artists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_top_artists(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingArtistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's top artists based on calculated affinity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.artists.get_users_top_artists(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopArtistsErrorBody
```

**Async**

```python
try:
    response = await async_client.artists.get_users_top_artists(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopArtistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>time_range</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"medium_term"</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingArtistObject](spotify_web_api/models/paging_artist_object.py)</code> -- Pages of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersTopArtistsErrorBody](spotify_web_api/errors/get_users_top_artists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unfollow_artists_users(type_: ItemType3OrStr, ids: str, *, body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the current user as a follower of one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.artists.unfollow_artists_users(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowArtistsUsersErrorBody
```

**Async**

```python
try:
    await async_client.artists.unfollow_artists_users(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowArtistsUsersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType3OrStr](spotify_web_api/models/enums/item_type3.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UnfollowArtistsOrUsersRequest](spotify_web_api/models/unfollow_artists_or_users_request.py) \| [UnfollowArtistsOrUsersRequestDict](spotify_web_api/models/unfollow_artists_or_users_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[UnfollowArtistsUsersErrorBody](spotify_web_api/errors/unfollow_artists_users_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Audiobooks

> Source: [Audiobooks](spotify_web_api/apis/audiobooks.py)

<details>
<summary><code>def check_users_saved_audiobooks(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more audiobooks are already saved in the current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.audiobooks.check_users_saved_audiobooks(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAudiobooksErrorBody
```

**Async**

```python
try:
    response = await async_client.audiobooks.check_users_saved_audiobooks(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAudiobooksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedAudiobooksErrorBody](spotify_web_api/errors/check_users_saved_audiobooks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_audiobook(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AudiobookObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.audiobooks.get_an_audiobook("7iHfbu1YPACw6oZPAFJtqe", market="ES")
    # TODO: Handle 'response' of type AudiobookObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAudiobookErrorBody
```

**Async**

```python
try:
    response = await async_client.audiobooks.get_an_audiobook("7iHfbu1YPACw6oZPAFJtqe", market="ES")
    # TODO: Handle 'response' of type AudiobookObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAudiobookErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AudiobookObject](spotify_web_api/models/audiobook_object.py)</code> -- An Audiobook

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnAudiobookErrorBody](spotify_web_api/errors/get_an_audiobook_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[BadRequest1](spotify_web_api/models/bad_request1.py)</code> |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 404 | <code>[NotFound1](spotify_web_api/models/not_found1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_audiobook_chapters(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSimplifiedChapterObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.audiobooks.get_audiobook_chapters("7iHfbu1YPACw6oZPAFJtqe", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedChapterObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudiobookChaptersErrorBody
```

**Async**

```python
try:
    response = await async_client.audiobooks.get_audiobook_chapters(
        "7iHfbu1YPACw6oZPAFJtqe", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingSimplifiedChapterObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudiobookChaptersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSimplifiedChapterObject](spotify_web_api/models/paging_simplified_chapter_object.py)</code> -- Pages of chapters

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAudiobookChaptersErrorBody](spotify_web_api/errors/get_audiobook_chapters_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multiple_audiobooks(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyAudiobooks</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.audiobooks.get_multiple_audiobooks(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe", market="ES"
    )
    # TODO: Handle 'response' of type ManyAudiobooks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleAudiobooksErrorBody
```

**Async**

```python
try:
    response = await async_client.audiobooks.get_multiple_audiobooks(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe", market="ES"
    )
    # TODO: Handle 'response' of type ManyAudiobooks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleAudiobooksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyAudiobooks](spotify_web_api/models/many_audiobooks.py)</code> -- A set of audiobooks. If one of the requested audiobooks is unavailable then you'll find a `null` item in the `audiobooks` array where the audiobook object would otherwise be.

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetMultipleAudiobooksErrorBody](spotify_web_api/errors/get_multiple_audiobooks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_audiobooks(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedAudiobookObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.audiobooks.get_users_saved_audiobooks(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedAudiobookObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAudiobooksErrorBody
```

**Async**

```python
try:
    response = await async_client.audiobooks.get_users_saved_audiobooks(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedAudiobookObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAudiobooksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedAudiobookObject](spotify_web_api/models/paging_saved_audiobook_object.py)</code> -- Pages of saved audiobooks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedAudiobooksErrorBody](spotify_web_api/errors/get_users_saved_audiobooks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_audiobooks_user(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more audiobooks from the Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.audiobooks.remove_audiobooks_user("18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAudiobooksUserErrorBody
```

**Async**

```python
try:
    await async_client.audiobooks.remove_audiobooks_user(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAudiobooksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveAudiobooksUserErrorBody](spotify_web_api/errors/remove_audiobooks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_audiobooks_user(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more audiobooks to the current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.audiobooks.save_audiobooks_user("18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAudiobooksUserErrorBody
```

**Async**

```python
try:
    await async_client.audiobooks.save_audiobooks_user(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAudiobooksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveAudiobooksUserErrorBody](spotify_web_api/errors/save_audiobooks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CategoriesApi

> Source: [CategoriesApi](spotify_web_api/apis/categories_api.py)

<details>
<summary><code>def get_a_categories_playlists(category_id: str, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingFeaturedPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of Spotify playlists tagged with a particular category.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories_api.get_a_categories_playlists("dinner", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingFeaturedPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetACategoriesPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.categories_api.get_a_categories_playlists("dinner", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingFeaturedPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetACategoriesPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>category_id</code> | <code>str</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingFeaturedPlaylistObject](spotify_web_api/models/paging_featured_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetACategoriesPlaylistsErrorBody](spotify_web_api/errors/get_a_categories_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_category(category_id: str, *, locale: str | None = None, request_options: RequestOptionsOrDict | None = None) -> CategoryObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories_api.get_a_category("dinner", locale="sv_SE")
    # TODO: Handle 'response' of type CategoryObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetACategoryErrorBody
```

**Async**

```python
try:
    response = await async_client.categories_api.get_a_category("dinner", locale="sv_SE")
    # TODO: Handle 'response' of type CategoryObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetACategoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>category_id</code> | <code>str</code> | Value sent with the request. |
| <code>locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoryObject](spotify_web_api/models/category_object.py)</code> -- A category

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetACategoryErrorBody](spotify_web_api/errors/get_a_category_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_categories(*, locale: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagedCategories</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories_api.get_categories(locale="sv_SE", limit=10, offset=5)
    # TODO: Handle 'response' of type PagedCategories
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCategoriesErrorBody
```

**Async**

```python
try:
    response = await async_client.categories_api.get_categories(locale="sv_SE", limit=10, offset=5)
    # TODO: Handle 'response' of type PagedCategories
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagedCategories](spotify_web_api/models/paged_categories.py)</code> -- A paged set of categories

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetCategoriesErrorBody](spotify_web_api/errors/get_categories_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Chapters

> Source: [Chapters](spotify_web_api/apis/chapters.py)

<details>
<summary><code>def get_a_chapter(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChapterObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single audiobook chapter. Chapters are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chapters.get_a_chapter("0D5wENdkdwbqlrHoaJ9g29", market="ES")
    # TODO: Handle 'response' of type ChapterObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAChapterErrorBody
```

**Async**

```python
try:
    response = await async_client.chapters.get_a_chapter("0D5wENdkdwbqlrHoaJ9g29", market="ES")
    # TODO: Handle 'response' of type ChapterObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAChapterErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChapterObject](spotify_web_api/models/chapter_object.py)</code> -- A Chapter

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAChapterErrorBody](spotify_web_api/errors/get_a_chapter_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_audiobook_chapters(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSimplifiedChapterObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chapters.get_audiobook_chapters("7iHfbu1YPACw6oZPAFJtqe", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedChapterObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudiobookChaptersErrorBody
```

**Async**

```python
try:
    response = await async_client.chapters.get_audiobook_chapters(
        "7iHfbu1YPACw6oZPAFJtqe", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingSimplifiedChapterObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudiobookChaptersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSimplifiedChapterObject](spotify_web_api/models/paging_simplified_chapter_object.py)</code> -- Pages of chapters

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAudiobookChaptersErrorBody](spotify_web_api/errors/get_audiobook_chapters_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_several_chapters(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyChapters</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs. Chapters are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chapters.get_several_chapters(
        "0IsXVP0JmcB2adSE338GkK,3ZXb8FKZGU0EHALYX6uCzU,0D5wENdkdwbqlrHoaJ9g29", market="ES"
    )
    # TODO: Handle 'response' of type ManyChapters
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSeveralChaptersErrorBody
```

**Async**

```python
try:
    response = await async_client.chapters.get_several_chapters(
        "0IsXVP0JmcB2adSE338GkK,3ZXb8FKZGU0EHALYX6uCzU,0D5wENdkdwbqlrHoaJ9g29", market="ES"
    )
    # TODO: Handle 'response' of type ManyChapters
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSeveralChaptersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyChapters](spotify_web_api/models/many_chapters.py)</code> -- A set of chapters

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetSeveralChaptersErrorBody](spotify_web_api/errors/get_several_chapters_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Episodes

> Source: [Episodes](spotify_web_api/apis/episodes.py)

<details>
<summary><code>def check_users_saved_episodes(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer)..

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.episodes.check_users_saved_episodes("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.episodes.check_users_saved_episodes("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedEpisodesErrorBody](spotify_web_api/errors/check_users_saved_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_shows_episodes(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSimplifiedEpisodeObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.episodes.get_a_shows_episodes("38bS44xjbVVZ3No3ByF1dJ", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAShowsEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.episodes.get_a_shows_episodes(
        "38bS44xjbVVZ3No3ByF1dJ", market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type PagingSimplifiedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAShowsEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSimplifiedEpisodeObject](spotify_web_api/models/paging_simplified_episode_object.py)</code> -- Pages of episodes

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAShowsEpisodesErrorBody](spotify_web_api/errors/get_a_shows_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_episode(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EpisodeObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single episode identified by its
unique Spotify ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.episodes.get_an_episode("512ojhOuo1ktJprKbVcKyQ", market="ES")
    # TODO: Handle 'response' of type EpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnEpisodeErrorBody
```

**Async**

```python
try:
    response = await async_client.episodes.get_an_episode("512ojhOuo1ktJprKbVcKyQ", market="ES")
    # TODO: Handle 'response' of type EpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnEpisodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EpisodeObject](spotify_web_api/models/episode_object.py)</code> -- An episode

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnEpisodeErrorBody](spotify_web_api/errors/get_an_episode_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multiple_episodes(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyEpisodes</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for several episodes based on their Spotify IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.episodes.get_multiple_episodes("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf", market="ES")
    # TODO: Handle 'response' of type ManyEpisodes
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.episodes.get_multiple_episodes(
        "77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf", market="ES"
    )
    # TODO: Handle 'response' of type ManyEpisodes
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyEpisodes](spotify_web_api/models/many_episodes.py)</code> -- A set of episodes

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetMultipleEpisodesErrorBody](spotify_web_api/errors/get_multiple_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_episodes(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedEpisodeObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the episodes saved in the current Spotify user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.episodes.get_users_saved_episodes(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.episodes.get_users_saved_episodes(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedEpisodeObject](spotify_web_api/models/paging_saved_episode_object.py)</code> -- Pages of episodes

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedEpisodesErrorBody](spotify_web_api/errors/get_users_saved_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_episodes_user(ids: str, *, body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more episodes from the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.episodes.remove_episodes_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveEpisodesUserErrorBody
```

**Async**

```python
try:
    await async_client.episodes.remove_episodes_user(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveEpisodesUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RemoveEpisodesRequest](spotify_web_api/models/remove_episodes_request.py) \| [RemoveEpisodesRequestDict](spotify_web_api/models/remove_episodes_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveEpisodesUserErrorBody](spotify_web_api/errors/remove_episodes_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_episodes_user(ids: str, *, body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more episodes to the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.episodes.save_episodes_user("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveEpisodesUserErrorBody
```

**Async**

```python
try:
    await async_client.episodes.save_episodes_user("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveEpisodesUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveEpisodesRequest](spotify_web_api/models/save_episodes_request.py) \| [SaveEpisodesRequestDict](spotify_web_api/models/save_episodes_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveEpisodesUserErrorBody](spotify_web_api/errors/save_episodes_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Genres

> Source: [Genres](spotify_web_api/apis/genres.py)

<details>
<summary><code>def get_recommendation_genres(*, request_options: RequestOptionsOrDict | None = None) -> ManyGenres</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a list of available genres seed parameter values for [recommendations](https://developer.spotify.com/documentation/web-api/reference/get-recommendations).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.genres.get_recommendation_genres()
    # TODO: Handle 'response' of type ManyGenres
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRecommendationGenresErrorBody
```

**Async**

```python
try:
    response = await async_client.genres.get_recommendation_genres()
    # TODO: Handle 'response' of type ManyGenres
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRecommendationGenresErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyGenres](spotify_web_api/models/many_genres.py)</code> -- A set of genres

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetRecommendationGenresErrorBody](spotify_web_api/errors/get_recommendation_genres_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Library

> Source: [Library](spotify_web_api/apis/library.py)

<details>
<summary><code>def change_playlist_details(playlist_id: str, *, body: PlaylistsRequest | PlaylistsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change a playlist's name and public/private state. (The user must, of
course, own the playlist.)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.change_playlist_details("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangePlaylistDetailsErrorBody
```

**Async**

```python
try:
    await async_client.library.change_playlist_details("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangePlaylistDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PlaylistsRequest](spotify_web_api/models/playlists_request.py) \| [PlaylistsRequestDict](spotify_web_api/models/playlists_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[ChangePlaylistDetailsErrorBody](spotify_web_api/errors/change_playlist_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_current_user_follows(type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check to see if the current user is following one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.check_current_user_follows(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCurrentUserFollowsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.check_current_user_follows(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCurrentUserFollowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType3OrStr](spotify_web_api/models/enums/item_type3.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckCurrentUserFollowsErrorBody](spotify_web_api/errors/check_current_user_follows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_users_saved_albums(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.check_users_saved_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.check_users_saved_albums(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedAlbumsErrorBody](spotify_web_api/errors/check_users_saved_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_users_saved_audiobooks(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more audiobooks are already saved in the current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.check_users_saved_audiobooks(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAudiobooksErrorBody
```

**Async**

```python
try:
    response = await async_client.library.check_users_saved_audiobooks(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedAudiobooksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedAudiobooksErrorBody](spotify_web_api/errors/check_users_saved_audiobooks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_users_saved_episodes(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer)..

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.check_users_saved_episodes("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.library.check_users_saved_episodes("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedEpisodesErrorBody](spotify_web_api/errors/check_users_saved_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_users_saved_shows(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more shows is already saved in the current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.check_users_saved_shows("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedShowsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.check_users_saved_shows("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedShowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedShowsErrorBody](spotify_web_api/errors/check_users_saved_shows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_users_saved_tracks(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.check_users_saved_tracks(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.library.check_users_saved_tracks(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedTracksErrorBody](spotify_web_api/errors/check_users_saved_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_playlist(user_id: str, *, body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a playlist for a Spotify user. (The playlist will be empty until
you [add tracks](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist).)
Each user is generally limited to a maximum of 11000 playlists.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.create_playlist("smedjan")
    # TODO: Handle 'response' of type PlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.library.create_playlist("smedjan")
    # TODO: Handle 'response' of type PlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UsersPlaylistsRequest](spotify_web_api/models/users_playlists_request.py) \| [UsersPlaylistsRequestDict](spotify_web_api/models/users_playlists_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistObject](spotify_web_api/models/playlist_object.py)</code> -- A playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CreatePlaylistErrorBody](spotify_web_api/errors/create_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def follow_artists_users(type_: ItemType2OrStr, ids: str, *, body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add the current user as a follower of one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.follow_artists_users(
        ItemType2.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowArtistsUsersErrorBody
```

**Async**

```python
try:
    await async_client.library.follow_artists_users(
        ItemType2.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowArtistsUsersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType2OrStr](spotify_web_api/models/enums/item_type2.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[FollowArtistsOrUsersRequest](spotify_web_api/models/follow_artists_or_users_request.py) \| [FollowArtistsOrUsersRequestDict](spotify_web_api/models/follow_artists_or_users_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[FollowArtistsUsersErrorBody](spotify_web_api/errors/follow_artists_users_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_list_of_current_users_playlists(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the playlists owned or followed by the current Spotify
user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_a_list_of_current_users_playlists(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAListOfCurrentUsersPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_a_list_of_current_users_playlists(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAListOfCurrentUsersPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingPlaylistObject](spotify_web_api/models/paging_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAListOfCurrentUsersPlaylistsErrorBody](spotify_web_api/errors/get_a_list_of_current_users_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_followed(type_: ItemType1OrStr, *, after: str | None = None, limit: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> CursorPagedArtists</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's followed artists.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_followed(ItemType1.ARTIST, after="0I2XqVXqHScXjHhk6AYYRe", limit=10)
    # TODO: Handle 'response' of type CursorPagedArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFollowedErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_followed(ItemType1.ARTIST, after="0I2XqVXqHScXjHhk6AYYRe", limit=10)
    # TODO: Handle 'response' of type CursorPagedArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFollowedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType1OrStr](spotify_web_api/models/enums/item_type1.py)</code> | Value sent with the request. |
| <code>after</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CursorPagedArtists](spotify_web_api/models/cursor_paged_artists.py)</code> -- A paged set of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetFollowedErrorBody](spotify_web_api/errors/get_followed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_albums(*, limit: int | None = 20, offset: int | None = 0, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PagingSavedAlbumObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the albums saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_saved_albums(limit=10, offset=5, market="ES")
    # TODO: Handle 'response' of type PagingSavedAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAlbumsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_saved_albums(limit=10, offset=5, market="ES")
    # TODO: Handle 'response' of type PagingSavedAlbumObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAlbumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedAlbumObject](spotify_web_api/models/paging_saved_album_object.py)</code> -- Pages of albums

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedAlbumsErrorBody](spotify_web_api/errors/get_users_saved_albums_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_audiobooks(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedAudiobookObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_saved_audiobooks(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedAudiobookObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAudiobooksErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_saved_audiobooks(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedAudiobookObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedAudiobooksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedAudiobookObject](spotify_web_api/models/paging_saved_audiobook_object.py)</code> -- Pages of saved audiobooks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedAudiobooksErrorBody](spotify_web_api/errors/get_users_saved_audiobooks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_episodes(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedEpisodeObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the episodes saved in the current Spotify user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_saved_episodes(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_saved_episodes(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedEpisodeObject](spotify_web_api/models/paging_saved_episode_object.py)</code> -- Pages of episodes

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedEpisodesErrorBody](spotify_web_api/errors/get_users_saved_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_shows(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedShowObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the number of shows returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_saved_shows(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedShowObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedShowsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_saved_shows(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedShowObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedShowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedShowObject](spotify_web_api/models/paging_saved_show_object.py)</code> -- Pages of shows

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedShowsErrorBody](spotify_web_api/errors/get_users_saved_shows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_tracks(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the songs saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_saved_tracks(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_saved_tracks(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedTrackObject](spotify_web_api/models/paging_saved_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedTracksErrorBody](spotify_web_api/errors/get_users_saved_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_top_artists(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingArtistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's top artists based on calculated affinity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_top_artists(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopArtistsErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_top_artists(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopArtistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>time_range</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"medium_term"</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingArtistObject](spotify_web_api/models/paging_artist_object.py)</code> -- Pages of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersTopArtistsErrorBody](spotify_web_api/errors/get_users_top_artists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_top_tracks(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's top tracks based on calculated affinity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.library.get_users_top_tracks(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.library.get_users_top_tracks(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>time_range</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"medium_term"</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingTrackObject](spotify_web_api/models/paging_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersTopTracksErrorBody](spotify_web_api/errors/get_users_top_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_albums_user(ids: str, *, body: RemoveAlbumsRequest | RemoveAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more albums from the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.remove_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAlbumsUserErrorBody
```

**Async**

```python
try:
    await async_client.library.remove_albums_user(
        "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAlbumsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RemoveAlbumsRequest](spotify_web_api/models/remove_albums_request.py) \| [RemoveAlbumsRequestDict](spotify_web_api/models/remove_albums_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveAlbumsUserErrorBody](spotify_web_api/errors/remove_albums_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_audiobooks_user(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more audiobooks from the Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.remove_audiobooks_user("18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAudiobooksUserErrorBody
```

**Async**

```python
try:
    await async_client.library.remove_audiobooks_user(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveAudiobooksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveAudiobooksUserErrorBody](spotify_web_api/errors/remove_audiobooks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_episodes_user(ids: str, *, body: RemoveEpisodesRequest | RemoveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more episodes from the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.remove_episodes_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveEpisodesUserErrorBody
```

**Async**

```python
try:
    await async_client.library.remove_episodes_user(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveEpisodesUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RemoveEpisodesRequest](spotify_web_api/models/remove_episodes_request.py) \| [RemoveEpisodesRequestDict](spotify_web_api/models/remove_episodes_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveEpisodesUserErrorBody](spotify_web_api/errors/remove_episodes_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_shows_user(ids: str, *, market: str | None = None, body: RemoveShowsRequest | RemoveShowsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete one or more shows from current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.remove_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ", market="ES")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveShowsUserErrorBody
```

**Async**

```python
try:
    await async_client.library.remove_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ", market="ES")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveShowsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[RemoveShowsRequest](spotify_web_api/models/remove_shows_request.py) \| [RemoveShowsRequestDict](spotify_web_api/models/remove_shows_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveShowsUserErrorBody](spotify_web_api/errors/remove_shows_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_tracks_user(ids: str, *, body: RemoveTracksRequest | RemoveTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more tracks from the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.remove_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksUserErrorBody
```

**Async**

```python
try:
    await async_client.library.remove_tracks_user(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RemoveTracksRequest](spotify_web_api/models/remove_tracks_request.py) \| [RemoveTracksRequestDict](spotify_web_api/models/remove_tracks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveTracksUserErrorBody](spotify_web_api/errors/remove_tracks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_albums_user(ids: str, *, body: SaveAlbumsRequest | SaveAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more albums to the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.save_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAlbumsUserErrorBody
```

**Async**

```python
try:
    await async_client.library.save_albums_user("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAlbumsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveAlbumsRequest](spotify_web_api/models/save_albums_request.py) \| [SaveAlbumsRequestDict](spotify_web_api/models/save_albums_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveAlbumsUserErrorBody](spotify_web_api/errors/save_albums_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_audiobooks_user(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more audiobooks to the current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.save_audiobooks_user("18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAudiobooksUserErrorBody
```

**Async**

```python
try:
    await async_client.library.save_audiobooks_user(
        "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveAudiobooksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveAudiobooksUserErrorBody](spotify_web_api/errors/save_audiobooks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_episodes_user(ids: str, *, body: SaveEpisodesRequest | SaveEpisodesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more episodes to the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.save_episodes_user("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveEpisodesUserErrorBody
```

**Async**

```python
try:
    await async_client.library.save_episodes_user("77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveEpisodesUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveEpisodesRequest](spotify_web_api/models/save_episodes_request.py) \| [SaveEpisodesRequestDict](spotify_web_api/models/save_episodes_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveEpisodesUserErrorBody](spotify_web_api/errors/save_episodes_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_shows_user(ids: str, *, body: SaveShowsRequest | SaveShowsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more shows to current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.save_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveShowsUserErrorBody
```

**Async**

```python
try:
    await async_client.library.save_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveShowsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveShowsRequest](spotify_web_api/models/save_shows_request.py) \| [SaveShowsRequestDict](spotify_web_api/models/save_shows_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveShowsUserErrorBody](spotify_web_api/errors/save_shows_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_tracks_user(ids: str, *, body: SaveTracksRequest | SaveTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more tracks to the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.save_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveTracksUserErrorBody
```

**Async**

```python
try:
    await async_client.library.save_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveTracksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveTracksRequest](spotify_web_api/models/save_tracks_request.py) \| [SaveTracksRequestDict](spotify_web_api/models/save_tracks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveTracksUserErrorBody](spotify_web_api/errors/save_tracks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unfollow_artists_users(type_: ItemType3OrStr, ids: str, *, body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the current user as a follower of one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.library.unfollow_artists_users(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowArtistsUsersErrorBody
```

**Async**

```python
try:
    await async_client.library.unfollow_artists_users(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowArtistsUsersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType3OrStr](spotify_web_api/models/enums/item_type3.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UnfollowArtistsOrUsersRequest](spotify_web_api/models/unfollow_artists_or_users_request.py) \| [UnfollowArtistsOrUsersRequestDict](spotify_web_api/models/unfollow_artists_or_users_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[UnfollowArtistsUsersErrorBody](spotify_web_api/errors/unfollow_artists_users_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## MarketsApi

> Source: [MarketsApi](spotify_web_api/apis/markets_api.py)

<details>
<summary><code>def get_available_markets(*, request_options: RequestOptionsOrDict | None = None) -> Markets</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the list of markets where Spotify is available.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.markets_api.get_available_markets()
    # TODO: Handle 'response' of type Markets
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAvailableMarketsErrorBody
```

**Async**

```python
try:
    response = await async_client.markets_api.get_available_markets()
    # TODO: Handle 'response' of type Markets
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAvailableMarketsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Markets](spotify_web_api/models/markets.py)</code> -- A markets object with an array of country codes

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAvailableMarketsErrorBody](spotify_web_api/errors/get_available_markets_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Player

> Source: [Player](spotify_web_api/apis/player.py)

<details>
<summary><code>def add_to_queue(uri: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an item to the end of the user's current playback queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.add_to_queue(
        "spotify:track:4iV5W9uYEdYUVa79Axb7Rh", device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddToQueueErrorBody
```

**Async**

```python
try:
    await async_client.player.add_to_queue(
        "spotify:track:4iV5W9uYEdYUVa79Axb7Rh", device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddToQueueErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uri</code> | <code>str</code> | Value sent with the request. |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[AddToQueueErrorBody](spotify_web_api/errors/add_to_queue_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_users_available_devices(*, request_options: RequestOptionsOrDict | None = None) -> ManyDevices</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get information about a user’s available Spotify Connect devices. Some device models are not supported and will not be listed in the API response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.player.get_a_users_available_devices()
    # TODO: Handle 'response' of type ManyDevices
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAUsersAvailableDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.player.get_a_users_available_devices()
    # TODO: Handle 'response' of type ManyDevices
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAUsersAvailableDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyDevices](spotify_web_api/models/many_devices.py)</code> -- A set of devices

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAUsersAvailableDevicesErrorBody](spotify_web_api/errors/get_a_users_available_devices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_information_about_the_users_current_playback(*, market: str | None = None, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None) -> CurrentlyPlayingContextObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get information about the user’s current playback state, including track or episode, progress, and active device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.player.get_information_about_the_users_current_playback(market="ES")
    # TODO: Handle 'response' of type CurrentlyPlayingContextObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInformationAboutTheUsersCurrentPlaybackErrorBody
```

**Async**

```python
try:
    response = await async_client.player.get_information_about_the_users_current_playback(market="ES")
    # TODO: Handle 'response' of type CurrentlyPlayingContextObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInformationAboutTheUsersCurrentPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>additional_types</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CurrentlyPlayingContextObject](spotify_web_api/models/currently_playing_context_object.py)</code> -- Information about playback

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetInformationAboutTheUsersCurrentPlaybackErrorBody](spotify_web_api/errors/get_information_about_the_users_current_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_queue(*, request_options: RequestOptionsOrDict | None = None) -> QueueObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the list of objects that make up the user's queue.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.player.get_queue()
    # TODO: Handle 'response' of type QueueObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetQueueErrorBody
```

**Async**

```python
try:
    response = await async_client.player.get_queue()
    # TODO: Handle 'response' of type QueueObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetQueueErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[QueueObject](spotify_web_api/models/queue_object.py)</code> -- Information about the queue

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetQueueErrorBody](spotify_web_api/errors/get_queue_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recently_played(*, limit: int | None = 20, after: int | None = None, before: int | None = None, request_options: RequestOptionsOrDict | None = None) -> CursorPagingPlayHistoryObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get tracks from the current user's recently played tracks.
_**Note**: Currently doesn't support podcast episodes._

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.player.get_recently_played(limit=10, after=1484811043508)
    # TODO: Handle 'response' of type CursorPagingPlayHistoryObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRecentlyPlayedErrorBody
```

**Async**

```python
try:
    response = await async_client.player.get_recently_played(limit=10, after=1484811043508)
    # TODO: Handle 'response' of type CursorPagingPlayHistoryObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRecentlyPlayedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>after</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>before</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CursorPagingPlayHistoryObject](spotify_web_api/models/cursor_paging_play_history_object.py)</code> -- A paged set of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetRecentlyPlayedErrorBody](spotify_web_api/errors/get_recently_played_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_the_users_currently_playing_track(*, market: str | None = None, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None) -> CurrentlyPlayingObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the object currently being played on the user's Spotify account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.player.get_the_users_currently_playing_track(market="ES")
    # TODO: Handle 'response' of type CurrentlyPlayingObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTheUsersCurrentlyPlayingTrackErrorBody
```

**Async**

```python
try:
    response = await async_client.player.get_the_users_currently_playing_track(market="ES")
    # TODO: Handle 'response' of type CurrentlyPlayingObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTheUsersCurrentlyPlayingTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>additional_types</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CurrentlyPlayingObject](spotify_web_api/models/currently_playing_object.py)</code> -- Information about the currently playing track

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetTheUsersCurrentlyPlayingTrackErrorBody](spotify_web_api/errors/get_the_users_currently_playing_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pause_a_users_playback(*, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.pause_a_users_playback(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PauseAUsersPlaybackErrorBody
```

**Async**

```python
try:
    await async_client.player.pause_a_users_playback(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PauseAUsersPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[PauseAUsersPlaybackErrorBody](spotify_web_api/errors/pause_a_users_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def seek_to_position_in_currently_playing_track(position_ms: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Seeks to the given position in the user’s currently playing track. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.seek_to_position_in_currently_playing_track(
        25000, device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SeekToPositionInCurrentlyPlayingTrackErrorBody
```

**Async**

```python
try:
    await async_client.player.seek_to_position_in_currently_playing_track(
        25000, device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SeekToPositionInCurrentlyPlayingTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>position_ms</code> | <code>int</code> | Value sent with the request. |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SeekToPositionInCurrentlyPlayingTrackErrorBody](spotify_web_api/errors/seek_to_position_in_currently_playing_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_repeat_mode_on_users_playback(state: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.set_repeat_mode_on_users_playback("context", device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetRepeatModeOnUsersPlaybackErrorBody
```

**Async**

```python
try:
    await async_client.player.set_repeat_mode_on_users_playback(
        "context", device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetRepeatModeOnUsersPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>state</code> | <code>str</code> | Value sent with the request. |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SetRepeatModeOnUsersPlaybackErrorBody](spotify_web_api/errors/set_repeat_mode_on_users_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_volume_for_users_playback(volume_percent: int, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the volume for the user’s current playback device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.set_volume_for_users_playback(50, device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetVolumeForUsersPlaybackErrorBody
```

**Async**

```python
try:
    await async_client.player.set_volume_for_users_playback(50, device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetVolumeForUsersPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>volume_percent</code> | <code>int</code> | Value sent with the request. |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SetVolumeForUsersPlaybackErrorBody](spotify_web_api/errors/set_volume_for_users_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def skip_users_playback_to_next_track(*, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.skip_users_playback_to_next_track(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SkipUsersPlaybackToNextTrackErrorBody
```

**Async**

```python
try:
    await async_client.player.skip_users_playback_to_next_track(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SkipUsersPlaybackToNextTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SkipUsersPlaybackToNextTrackErrorBody](spotify_web_api/errors/skip_users_playback_to_next_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def skip_users_playback_to_previous_track(*, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.skip_users_playback_to_previous_track(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SkipUsersPlaybackToPreviousTrackErrorBody
```

**Async**

```python
try:
    await async_client.player.skip_users_playback_to_previous_track(
        device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SkipUsersPlaybackToPreviousTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SkipUsersPlaybackToPreviousTrackErrorBody](spotify_web_api/errors/skip_users_playback_to_previous_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_a_users_playback(*, device_id: str | None = None, body: StartOrResumePlaybackRequest | StartOrResumePlaybackRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start a new context or resume current playback on the user's active device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.start_a_users_playback(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartAUsersPlaybackErrorBody
```

**Async**

```python
try:
    await async_client.player.start_a_users_playback(device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartAUsersPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[StartOrResumePlaybackRequest](spotify_web_api/models/start_or_resume_playback_request.py) \| [StartOrResumePlaybackRequestDict](spotify_web_api/models/start_or_resume_playback_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[StartAUsersPlaybackErrorBody](spotify_web_api/errors/start_a_users_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def toggle_shuffle_for_users_playback(state: bool, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.toggle_shuffle_for_users_playback(True, device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ToggleShuffleForUsersPlaybackErrorBody
```

**Async**

```python
try:
    await async_client.player.toggle_shuffle_for_users_playback(
        True, device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ToggleShuffleForUsersPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>state</code> | <code>bool</code> | Value sent with the request. |
| <code>device_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[ToggleShuffleForUsersPlaybackErrorBody](spotify_web_api/errors/toggle_shuffle_for_users_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_a_users_playback(*, body: MePlayerRequest | MePlayerRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transfer playback to a new device and optionally begin playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.player.transfer_a_users_playback()
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferAUsersPlaybackErrorBody
```

**Async**

```python
try:
    await async_client.player.transfer_a_users_playback()
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferAUsersPlaybackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[MePlayerRequest](spotify_web_api/models/me_player_request.py) \| [MePlayerRequestDict](spotify_web_api/models/me_player_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[TransferAUsersPlaybackErrorBody](spotify_web_api/errors/transfer_a_users_playback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Playlists

> Source: [Playlists](spotify_web_api/apis/playlists.py)

<details>
<summary><code>def add_tracks_to_playlist(playlist_id: str, *, position: int | None = None, uris: str | None = None, body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistSnapshotId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add one or more items to a user's playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.add_tracks_to_playlist(
        "3cEYpjA9oz9GiPac4AsH4n",
        position=0,
        uris="spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M",
    )
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddTracksToPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.add_tracks_to_playlist(
        "3cEYpjA9oz9GiPac4AsH4n",
        position=0,
        uris="spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M",
    )
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddTracksToPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>position</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>uris</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[PlaylistsTracksRequest](spotify_web_api/models/playlists_tracks_request.py) \| [PlaylistsTracksRequestDict](spotify_web_api/models/playlists_tracks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistSnapshotId](spotify_web_api/models/playlist_snapshot_id.py)</code> -- A snapshot ID for the playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[AddTracksToPlaylistErrorBody](spotify_web_api/errors/add_tracks_to_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_playlist_details(playlist_id: str, *, body: PlaylistsRequest | PlaylistsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change a playlist's name and public/private state. (The user must, of
course, own the playlist.)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.playlists.change_playlist_details("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangePlaylistDetailsErrorBody
```

**Async**

```python
try:
    await async_client.playlists.change_playlist_details("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangePlaylistDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PlaylistsRequest](spotify_web_api/models/playlists_request.py) \| [PlaylistsRequestDict](spotify_web_api/models/playlists_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[ChangePlaylistDetailsErrorBody](spotify_web_api/errors/change_playlist_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_if_user_follows_playlist(playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check to see if one or more Spotify users are following a specified playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.check_if_user_follows_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", "jmperezperez,thelinmichael,wizzler"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckIfUserFollowsPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.check_if_user_follows_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", "jmperezperez,thelinmichael,wizzler"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckIfUserFollowsPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckIfUserFollowsPlaylistErrorBody](spotify_web_api/errors/check_if_user_follows_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_playlist(user_id: str, *, body: UsersPlaylistsRequest | UsersPlaylistsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a playlist for a Spotify user. (The playlist will be empty until
you [add tracks](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist).)
Each user is generally limited to a maximum of 11000 playlists.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.create_playlist("smedjan")
    # TODO: Handle 'response' of type PlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.create_playlist("smedjan")
    # TODO: Handle 'response' of type PlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UsersPlaylistsRequest](spotify_web_api/models/users_playlists_request.py) \| [UsersPlaylistsRequestDict](spotify_web_api/models/users_playlists_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistObject](spotify_web_api/models/playlist_object.py)</code> -- A playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CreatePlaylistErrorBody](spotify_web_api/errors/create_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def follow_playlist(playlist_id: str, *, body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add the current user as a follower of a playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.playlists.follow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowPlaylistErrorBody
```

**Async**

```python
try:
    await async_client.playlists.follow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PlaylistsFollowersRequest](spotify_web_api/models/playlists_followers_request.py) \| [PlaylistsFollowersRequestDict](spotify_web_api/models/playlists_followers_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[FollowPlaylistErrorBody](spotify_web_api/errors/follow_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_categories_playlists(category_id: str, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingFeaturedPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of Spotify playlists tagged with a particular category.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_a_categories_playlists("dinner", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingFeaturedPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetACategoriesPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_a_categories_playlists("dinner", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingFeaturedPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetACategoriesPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>category_id</code> | <code>str</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingFeaturedPlaylistObject](spotify_web_api/models/paging_featured_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetACategoriesPlaylistsErrorBody](spotify_web_api/errors/get_a_categories_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_list_of_current_users_playlists(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the playlists owned or followed by the current Spotify
user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_a_list_of_current_users_playlists(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAListOfCurrentUsersPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_a_list_of_current_users_playlists(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAListOfCurrentUsersPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingPlaylistObject](spotify_web_api/models/paging_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAListOfCurrentUsersPlaylistsErrorBody](spotify_web_api/errors/get_a_list_of_current_users_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_featured_playlists(*, locale: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingFeaturedPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_featured_playlists(locale="sv_SE", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingFeaturedPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeaturedPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_featured_playlists(locale="sv_SE", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingFeaturedPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeaturedPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingFeaturedPlaylistObject](spotify_web_api/models/paging_featured_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetFeaturedPlaylistsErrorBody](spotify_web_api/errors/get_featured_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_list_users_playlists(user_id: str, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the playlists owned or followed by a Spotify user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_list_users_playlists("smedjan", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListUsersPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_list_users_playlists("smedjan", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListUsersPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_id</code> | <code>str</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingPlaylistObject](spotify_web_api/models/paging_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetListUsersPlaylistsErrorBody](spotify_web_api/errors/get_list_users_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_playlist(playlist_id: str, *, market: str | None = None, fields: str | None = None, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a playlist owned by a Spotify user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", market="ES", fields="items(added_by.id,track(name,href,album(name,href)))"
    )
    # TODO: Handle 'response' of type PlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", market="ES", fields="items(added_by.id,track(name,href,album(name,href)))"
    )
    # TODO: Handle 'response' of type PlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>additional_types</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistObject](spotify_web_api/models/playlist_object.py)</code> -- A playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetPlaylistErrorBody](spotify_web_api/errors/get_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_playlist_cover(playlist_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[ImageObject]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current image associated with a specific playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_playlist_cover("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type list[ImageObject]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistCoverErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_playlist_cover("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type list[ImageObject]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistCoverErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ImageObject](spotify_web_api/models/image_object.py)&#93;</code> -- A set of images

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetPlaylistCoverErrorBody](spotify_web_api/errors/get_playlist_cover_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_playlists_tracks(playlist_id: str, *, market: str | None = None, fields: str | None = None, limit: int | None = 20, offset: int | None = 0, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PagingPlaylistTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get full details of the items of a playlist owned by a Spotify user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.get_playlists_tracks(
        "3cEYpjA9oz9GiPac4AsH4n",
        market="ES",
        fields="items(added_by.id,track(name,href,album(name,href)))",
        limit=10,
        offset=5,
    )
    # TODO: Handle 'response' of type PagingPlaylistTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistsTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.get_playlists_tracks(
        "3cEYpjA9oz9GiPac4AsH4n",
        market="ES",
        fields="items(added_by.id,track(name,href,album(name,href)))",
        limit=10,
        offset=5,
    )
    # TODO: Handle 'response' of type PagingPlaylistTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistsTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>additional_types</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingPlaylistTrackObject](spotify_web_api/models/paging_playlist_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetPlaylistsTracksErrorBody](spotify_web_api/errors/get_playlists_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_tracks_playlist(playlist_id: str, *, body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistSnapshotId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more items from a user's playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.remove_tracks_playlist("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.remove_tracks_playlist("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PlaylistsTracksRequest2](spotify_web_api/models/playlists_tracks_request2.py) \| [PlaylistsTracksRequest2Dict](spotify_web_api/models/playlists_tracks_request2.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistSnapshotId](spotify_web_api/models/playlist_snapshot_id.py)</code> -- A snapshot ID for the playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveTracksPlaylistErrorBody](spotify_web_api/errors/remove_tracks_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reorder_or_replace_playlists_tracks(playlist_id: str, *, uris: str | None = None, body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistSnapshotId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Either reorder or replace items in a playlist depending on the request's parameters.
To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body.
To replace items, include `uris` as either a query parameter or in the request's body.
Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist.
<br/>
**Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters.
These operations can't be applied together in a single request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.playlists.reorder_or_replace_playlists_tracks("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReorderOrReplacePlaylistsTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.playlists.reorder_or_replace_playlists_tracks("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReorderOrReplacePlaylistsTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>uris</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[PlaylistsTracksRequest1](spotify_web_api/models/playlists_tracks_request1.py) \| [PlaylistsTracksRequest1Dict](spotify_web_api/models/playlists_tracks_request1.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistSnapshotId](spotify_web_api/models/playlist_snapshot_id.py)</code> -- A snapshot ID for the playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[ReorderOrReplacePlaylistsTracksErrorBody](spotify_web_api/errors/reorder_or_replace_playlists_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unfollow_playlist(playlist_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the current user as a follower of a playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.playlists.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowPlaylistErrorBody
```

**Async**

```python
try:
    await async_client.playlists.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[UnfollowPlaylistErrorBody](spotify_web_api/errors/unfollow_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upload_custom_playlist_cover(playlist_id: str, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Replace the image used to represent a specific playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.playlists.upload_custom_playlist_cover("3cEYpjA9oz9GiPac4AsH4n", {})
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadCustomPlaylistCoverErrorBody
```

**Async**

```python
try:
    await async_client.playlists.upload_custom_playlist_cover("3cEYpjA9oz9GiPac4AsH4n", {})
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadCustomPlaylistCoverErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[UploadCustomPlaylistCoverErrorBody](spotify_web_api/errors/upload_custom_playlist_cover_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Search

> Source: [Search](spotify_web_api/apis/search.py)

<details>
<summary><code>def search(q: str, type_: list[ItemtypeOrStr], *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, include_external: IncludeExternalOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> SearchItems</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks
that match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search.search(
        "remaster%20track:Doxy%20artist:Miles%20Davis", [Itemtype.ALBUM], market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type SearchItems
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchErrorBody
```

**Async**

```python
try:
    response = await async_client.search.search(
        "remaster%20track:Doxy%20artist:Miles%20Davis", [Itemtype.ALBUM], market="ES", limit=10, offset=5
    )
    # TODO: Handle 'response' of type SearchItems
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>q</code> | <code>str</code> | Value sent with the request. |
| <code>type_</code> | <code>list&#91;[ItemtypeOrStr](spotify_web_api/models/enums/itemtype.py)&#93;</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>include_external</code> | <code>[IncludeExternalOrStr](spotify_web_api/models/enums/include_external.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SearchItems](spotify_web_api/models/search_items.py)</code> -- Search response

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SearchErrorBody](spotify_web_api/errors/search_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Shows

> Source: [Shows](spotify_web_api/apis/shows.py)

<details>
<summary><code>def check_users_saved_shows(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more shows is already saved in the current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shows.check_users_saved_shows("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedShowsErrorBody
```

**Async**

```python
try:
    response = await async_client.shows.check_users_saved_shows("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedShowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedShowsErrorBody](spotify_web_api/errors/check_users_saved_shows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_show(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ShowObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single show identified by its
unique Spotify ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shows.get_a_show("38bS44xjbVVZ3No3ByF1dJ", market="ES")
    # TODO: Handle 'response' of type ShowObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAShowErrorBody
```

**Async**

```python
try:
    response = await async_client.shows.get_a_show("38bS44xjbVVZ3No3ByF1dJ", market="ES")
    # TODO: Handle 'response' of type ShowObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAShowErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ShowObject](spotify_web_api/models/show_object.py)</code> -- A show

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAShowErrorBody](spotify_web_api/errors/get_a_show_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_shows_episodes(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSimplifiedEpisodeObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shows.get_a_shows_episodes("38bS44xjbVVZ3No3ByF1dJ", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAShowsEpisodesErrorBody
```

**Async**

```python
try:
    response = await async_client.shows.get_a_shows_episodes("38bS44xjbVVZ3No3ByF1dJ", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedEpisodeObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAShowsEpisodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSimplifiedEpisodeObject](spotify_web_api/models/paging_simplified_episode_object.py)</code> -- Pages of episodes

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAShowsEpisodesErrorBody](spotify_web_api/errors/get_a_shows_episodes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multiple_shows(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManySimplifiedShows</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for several shows based on their Spotify IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shows.get_multiple_shows("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ", market="ES")
    # TODO: Handle 'response' of type ManySimplifiedShows
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleShowsErrorBody
```

**Async**

```python
try:
    response = await async_client.shows.get_multiple_shows("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ", market="ES")
    # TODO: Handle 'response' of type ManySimplifiedShows
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMultipleShowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManySimplifiedShows](spotify_web_api/models/many_simplified_shows.py)</code> -- A set of shows

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetMultipleShowsErrorBody](spotify_web_api/errors/get_multiple_shows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_shows(*, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedShowObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the number of shows returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shows.get_users_saved_shows(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedShowObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedShowsErrorBody
```

**Async**

```python
try:
    response = await async_client.shows.get_users_saved_shows(limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedShowObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedShowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedShowObject](spotify_web_api/models/paging_saved_show_object.py)</code> -- Pages of shows

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedShowsErrorBody](spotify_web_api/errors/get_users_saved_shows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_shows_user(ids: str, *, market: str | None = None, body: RemoveShowsRequest | RemoveShowsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete one or more shows from current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.shows.remove_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ", market="ES")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveShowsUserErrorBody
```

**Async**

```python
try:
    await async_client.shows.remove_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ", market="ES")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveShowsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[RemoveShowsRequest](spotify_web_api/models/remove_shows_request.py) \| [RemoveShowsRequestDict](spotify_web_api/models/remove_shows_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveShowsUserErrorBody](spotify_web_api/errors/remove_shows_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_shows_user(ids: str, *, body: SaveShowsRequest | SaveShowsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more shows to current Spotify user's library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.shows.save_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveShowsUserErrorBody
```

**Async**

```python
try:
    await async_client.shows.save_shows_user("5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveShowsUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveShowsRequest](spotify_web_api/models/save_shows_request.py) \| [SaveShowsRequestDict](spotify_web_api/models/save_shows_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveShowsUserErrorBody](spotify_web_api/errors/save_shows_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Tracks

> Source: [Tracks](spotify_web_api/apis/tracks.py)

<details>
<summary><code>def add_tracks_to_playlist(playlist_id: str, *, position: int | None = None, uris: str | None = None, body: PlaylistsTracksRequest | PlaylistsTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistSnapshotId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add one or more items to a user's playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.add_tracks_to_playlist(
        "3cEYpjA9oz9GiPac4AsH4n",
        position=0,
        uris="spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M",
    )
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddTracksToPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.add_tracks_to_playlist(
        "3cEYpjA9oz9GiPac4AsH4n",
        position=0,
        uris="spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M",
    )
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddTracksToPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>position</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>uris</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[PlaylistsTracksRequest](spotify_web_api/models/playlists_tracks_request.py) \| [PlaylistsTracksRequestDict](spotify_web_api/models/playlists_tracks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistSnapshotId](spotify_web_api/models/playlist_snapshot_id.py)</code> -- A snapshot ID for the playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[AddTracksToPlaylistErrorBody](spotify_web_api/errors/add_tracks_to_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_users_saved_tracks(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.check_users_saved_tracks(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.check_users_saved_tracks(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckUsersSavedTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckUsersSavedTracksErrorBody](spotify_web_api/errors/check_users_saved_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_albums_tracks(id_: str, *, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSimplifiedTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an album’s tracks.
Optional parameters can be used to limit the number of tracks returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_an_albums_tracks("4aawyAB9vmqN3uQ7FjRGTy", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAlbumsTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_an_albums_tracks("4aawyAB9vmqN3uQ7FjRGTy", market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSimplifiedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnAlbumsTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSimplifiedTrackObject](spotify_web_api/models/paging_simplified_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnAlbumsTracksErrorBody](spotify_web_api/errors/get_an_albums_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_an_artists_top_tracks(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyTracks</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information about an artist's top tracks by country.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_an_artists_top_tracks("0TnOYISbd1XYRBk9myaseg", market="ES")
    # TODO: Handle 'response' of type ManyTracks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsTopTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_an_artists_top_tracks("0TnOYISbd1XYRBk9myaseg", market="ES")
    # TODO: Handle 'response' of type ManyTracks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnArtistsTopTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyTracks](spotify_web_api/models/many_tracks.py)</code> -- A set of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAnArtistsTopTracksErrorBody](spotify_web_api/errors/get_an_artists_top_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_audio_analysis(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> AudioAnalysisObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_audio_analysis("11dFghVXANMlKmJXsNCbNl")
    # TODO: Handle 'response' of type AudioAnalysisObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudioAnalysisErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_audio_analysis("11dFghVXANMlKmJXsNCbNl")
    # TODO: Handle 'response' of type AudioAnalysisObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudioAnalysisErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AudioAnalysisObject](spotify_web_api/models/audio_analysis_object.py)</code> -- Audio analysis for one track

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAudioAnalysisErrorBody](spotify_web_api/errors/get_audio_analysis_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_audio_features(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> AudioFeaturesObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get audio feature information for a single track identified by its unique
Spotify ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_audio_features("11dFghVXANMlKmJXsNCbNl")
    # TODO: Handle 'response' of type AudioFeaturesObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudioFeaturesErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_audio_features("11dFghVXANMlKmJXsNCbNl")
    # TODO: Handle 'response' of type AudioFeaturesObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAudioFeaturesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AudioFeaturesObject](spotify_web_api/models/audio_features_object.py)</code> -- Audio features for one track

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetAudioFeaturesErrorBody](spotify_web_api/errors/get_audio_features_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_playlists_tracks(playlist_id: str, *, market: str | None = None, fields: str | None = None, limit: int | None = 20, offset: int | None = 0, additional_types: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PagingPlaylistTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get full details of the items of a playlist owned by a Spotify user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_playlists_tracks(
        "3cEYpjA9oz9GiPac4AsH4n",
        market="ES",
        fields="items(added_by.id,track(name,href,album(name,href)))",
        limit=10,
        offset=5,
    )
    # TODO: Handle 'response' of type PagingPlaylistTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistsTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_playlists_tracks(
        "3cEYpjA9oz9GiPac4AsH4n",
        market="ES",
        fields="items(added_by.id,track(name,href,album(name,href)))",
        limit=10,
        offset=5,
    )
    # TODO: Handle 'response' of type PagingPlaylistTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPlaylistsTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>additional_types</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingPlaylistTrackObject](spotify_web_api/models/paging_playlist_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetPlaylistsTracksErrorBody](spotify_web_api/errors/get_playlists_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recommendations(*, limit: int | None = 20, market: str | None = None, seed_artists: str | None = None, seed_genres: str | None = None, seed_tracks: str | None = None, min_acousticness: float | None = None, max_acousticness: float | None = None, target_acousticness: float | None = None, min_danceability: float | None = None, max_danceability: float | None = None, target_danceability: float | None = None, min_duration_ms: int | None = None, max_duration_ms: int | None = None, target_duration_ms: int | None = None, min_energy: float | None = None, max_energy: float | None = None, target_energy: float | None = None, min_instrumentalness: float | None = None, max_instrumentalness: float | None = None, target_instrumentalness: float | None = None, min_key: int | None = None, max_key: int | None = None, target_key: int | None = None, min_liveness: float | None = None, max_liveness: float | None = None, target_liveness: float | None = None, min_loudness: float | None = None, max_loudness: float | None = None, target_loudness: float | None = None, min_mode: int | None = None, max_mode: int | None = None, target_mode: int | None = None, min_popularity: int | None = None, max_popularity: int | None = None, target_popularity: int | None = None, min_speechiness: float | None = None, max_speechiness: float | None = None, target_speechiness: float | None = None, min_tempo: float | None = None, max_tempo: float | None = None, target_tempo: float | None = None, min_time_signature: int | None = None, max_time_signature: int | None = None, target_time_signature: int | None = None, min_valence: float | None = None, max_valence: float | None = None, target_valence: float | None = None, request_options: RequestOptionsOrDict | None = None) -> RecommendationsObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.

For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_recommendations(
        limit=10,
        market="ES",
        seed_artists="4NHQUGzhtTLFvgF5SZesLK",
        seed_genres="classical,country",
        seed_tracks="0c6xIDDpzE81m2q797ordA",
    )
    # TODO: Handle 'response' of type RecommendationsObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRecommendationsErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_recommendations(
        limit=10,
        market="ES",
        seed_artists="4NHQUGzhtTLFvgF5SZesLK",
        seed_genres="classical,country",
        seed_tracks="0c6xIDDpzE81m2q797ordA",
    )
    # TODO: Handle 'response' of type RecommendationsObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>seed_artists</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>seed_genres</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>seed_tracks</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_acousticness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_acousticness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_acousticness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_danceability</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_danceability</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_danceability</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_duration_ms</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_duration_ms</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_duration_ms</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_energy</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_energy</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_energy</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_instrumentalness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_instrumentalness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_instrumentalness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_key</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_key</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_key</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_liveness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_liveness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_liveness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_loudness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_loudness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_loudness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_mode</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_mode</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_mode</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_popularity</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_popularity</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_popularity</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_speechiness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_speechiness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_speechiness</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_tempo</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_tempo</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_tempo</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_time_signature</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_time_signature</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_time_signature</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>min_valence</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>max_valence</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>target_valence</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RecommendationsObject](spotify_web_api/models/recommendations_object.py)</code> -- A set of recommendations

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetRecommendationsErrorBody](spotify_web_api/errors/get_recommendations_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_several_audio_features(ids: str, *, request_options: RequestOptionsOrDict | None = None) -> ManyAudioFeatures</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get audio features for multiple tracks based on their Spotify IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_several_audio_features(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
    # TODO: Handle 'response' of type ManyAudioFeatures
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSeveralAudioFeaturesErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_several_audio_features(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
    )
    # TODO: Handle 'response' of type ManyAudioFeatures
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSeveralAudioFeaturesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyAudioFeatures](spotify_web_api/models/many_audio_features.py)</code> -- A set of audio features

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetSeveralAudioFeaturesErrorBody](spotify_web_api/errors/get_several_audio_features_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_several_tracks(ids: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ManyTracks</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for multiple tracks based on their Spotify IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_several_tracks(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B", market="ES"
    )
    # TODO: Handle 'response' of type ManyTracks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSeveralTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_several_tracks(
        "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B", market="ES"
    )
    # TODO: Handle 'response' of type ManyTracks
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSeveralTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ManyTracks](spotify_web_api/models/many_tracks.py)</code> -- A set of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetSeveralTracksErrorBody](spotify_web_api/errors/get_several_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track(id_: str, *, market: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Spotify catalog information for a single track identified by its
unique Spotify ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_track("11dFghVXANMlKmJXsNCbNl", market="ES")
    # TODO: Handle 'response' of type TrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_track("11dFghVXANMlKmJXsNCbNl", market="ES")
    # TODO: Handle 'response' of type TrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TrackObject](spotify_web_api/models/track_object.py)</code> -- A track

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetTrackErrorBody](spotify_web_api/errors/get_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_saved_tracks(*, market: str | None = None, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingSavedTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the songs saved in the current Spotify user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_users_saved_tracks(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_users_saved_tracks(market="ES", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingSavedTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersSavedTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>market</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingSavedTrackObject](spotify_web_api/models/paging_saved_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersSavedTracksErrorBody](spotify_web_api/errors/get_users_saved_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_top_tracks(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's top tracks based on calculated affinity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.get_users_top_tracks(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.get_users_top_tracks(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>time_range</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"medium_term"</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingTrackObject](spotify_web_api/models/paging_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersTopTracksErrorBody](spotify_web_api/errors/get_users_top_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_tracks_playlist(playlist_id: str, *, body: PlaylistsTracksRequest2 | PlaylistsTracksRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistSnapshotId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more items from a user's playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.remove_tracks_playlist("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.remove_tracks_playlist("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PlaylistsTracksRequest2](spotify_web_api/models/playlists_tracks_request2.py) \| [PlaylistsTracksRequest2Dict](spotify_web_api/models/playlists_tracks_request2.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistSnapshotId](spotify_web_api/models/playlist_snapshot_id.py)</code> -- A snapshot ID for the playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveTracksPlaylistErrorBody](spotify_web_api/errors/remove_tracks_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_tracks_user(ids: str, *, body: RemoveTracksRequest | RemoveTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more tracks from the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.tracks.remove_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksUserErrorBody
```

**Async**

```python
try:
    await async_client.tracks.remove_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveTracksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RemoveTracksRequest](spotify_web_api/models/remove_tracks_request.py) \| [RemoveTracksRequestDict](spotify_web_api/models/remove_tracks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[RemoveTracksUserErrorBody](spotify_web_api/errors/remove_tracks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reorder_or_replace_playlists_tracks(playlist_id: str, *, uris: str | None = None, body: PlaylistsTracksRequest1 | PlaylistsTracksRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> PlaylistSnapshotId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Either reorder or replace items in a playlist depending on the request's parameters.
To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body.
To replace items, include `uris` as either a query parameter or in the request's body.
Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist.
<br/>
**Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters.
These operations can't be applied together in a single request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tracks.reorder_or_replace_playlists_tracks("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReorderOrReplacePlaylistsTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.tracks.reorder_or_replace_playlists_tracks("3cEYpjA9oz9GiPac4AsH4n")
    # TODO: Handle 'response' of type PlaylistSnapshotId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReorderOrReplacePlaylistsTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>uris</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[PlaylistsTracksRequest1](spotify_web_api/models/playlists_tracks_request1.py) \| [PlaylistsTracksRequest1Dict](spotify_web_api/models/playlists_tracks_request1.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlaylistSnapshotId](spotify_web_api/models/playlist_snapshot_id.py)</code> -- A snapshot ID for the playlist

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[ReorderOrReplacePlaylistsTracksErrorBody](spotify_web_api/errors/reorder_or_replace_playlists_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def save_tracks_user(ids: str, *, body: SaveTracksRequest | SaveTracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save one or more tracks to the current user's 'Your Music' library.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.tracks.save_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveTracksUserErrorBody
```

**Async**

```python
try:
    await async_client.tracks.save_tracks_user("7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SaveTracksUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[SaveTracksRequest](spotify_web_api/models/save_tracks_request.py) \| [SaveTracksRequestDict](spotify_web_api/models/save_tracks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[SaveTracksUserErrorBody](spotify_web_api/errors/save_tracks_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Users

> Source: [Users](spotify_web_api/apis/users.py)

<details>
<summary><code>def check_current_user_follows(type_: ItemType3OrStr, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check to see if the current user is following one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.check_current_user_follows(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCurrentUserFollowsErrorBody
```

**Async**

```python
try:
    response = await async_client.users.check_current_user_follows(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCurrentUserFollowsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType3OrStr](spotify_web_api/models/enums/item_type3.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckCurrentUserFollowsErrorBody](spotify_web_api/errors/check_current_user_follows_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_if_user_follows_playlist(playlist_id: str, ids: str, *, request_options: RequestOptionsOrDict | None = None) -> list[bool]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check to see if one or more Spotify users are following a specified playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.check_if_user_follows_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", "jmperezperez,thelinmichael,wizzler"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckIfUserFollowsPlaylistErrorBody
```

**Async**

```python
try:
    response = await async_client.users.check_if_user_follows_playlist(
        "3cEYpjA9oz9GiPac4AsH4n", "jmperezperez,thelinmichael,wizzler"
    )
    # TODO: Handle 'response' of type list[bool]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckIfUserFollowsPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;bool&#93;</code> -- Array of booleans

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[CheckIfUserFollowsPlaylistErrorBody](spotify_web_api/errors/check_if_user_follows_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def follow_artists_users(type_: ItemType2OrStr, ids: str, *, body: FollowArtistsOrUsersRequest | FollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add the current user as a follower of one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.follow_artists_users(
        ItemType2.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowArtistsUsersErrorBody
```

**Async**

```python
try:
    await async_client.users.follow_artists_users(
        ItemType2.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowArtistsUsersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType2OrStr](spotify_web_api/models/enums/item_type2.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[FollowArtistsOrUsersRequest](spotify_web_api/models/follow_artists_or_users_request.py) \| [FollowArtistsOrUsersRequestDict](spotify_web_api/models/follow_artists_or_users_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[FollowArtistsUsersErrorBody](spotify_web_api/errors/follow_artists_users_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def follow_playlist(playlist_id: str, *, body: PlaylistsFollowersRequest | PlaylistsFollowersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add the current user as a follower of a playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.follow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowPlaylistErrorBody
```

**Async**

```python
try:
    await async_client.users.follow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FollowPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PlaylistsFollowersRequest](spotify_web_api/models/playlists_followers_request.py) \| [PlaylistsFollowersRequestDict](spotify_web_api/models/playlists_followers_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[FollowPlaylistErrorBody](spotify_web_api/errors/follow_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_current_users_profile(*, request_options: RequestOptionsOrDict | None = None) -> PrivateUserObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get detailed profile information about the current user (including the
current user's username).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_current_users_profile()
    # TODO: Handle 'response' of type PrivateUserObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrentUsersProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_current_users_profile()
    # TODO: Handle 'response' of type PrivateUserObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrentUsersProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PrivateUserObject](spotify_web_api/models/private_user_object.py)</code> -- A user

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetCurrentUsersProfileErrorBody](spotify_web_api/errors/get_current_users_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_followed(type_: ItemType1OrStr, *, after: str | None = None, limit: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> CursorPagedArtists</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's followed artists.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_followed(ItemType1.ARTIST, after="0I2XqVXqHScXjHhk6AYYRe", limit=10)
    # TODO: Handle 'response' of type CursorPagedArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFollowedErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_followed(ItemType1.ARTIST, after="0I2XqVXqHScXjHhk6AYYRe", limit=10)
    # TODO: Handle 'response' of type CursorPagedArtists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFollowedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType1OrStr](spotify_web_api/models/enums/item_type1.py)</code> | Value sent with the request. |
| <code>after</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CursorPagedArtists](spotify_web_api/models/cursor_paged_artists.py)</code> -- A paged set of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetFollowedErrorBody](spotify_web_api/errors/get_followed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_list_users_playlists(user_id: str, *, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingPlaylistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of the playlists owned or followed by a Spotify user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_list_users_playlists("smedjan", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListUsersPlaylistsErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_list_users_playlists("smedjan", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingPlaylistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListUsersPlaylistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_id</code> | <code>str</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingPlaylistObject](spotify_web_api/models/paging_playlist_object.py)</code> -- A paged set of playlists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetListUsersPlaylistsErrorBody](spotify_web_api/errors/get_list_users_playlists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_profile(user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> PublicUserObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get public profile information about a Spotify user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_users_profile("smedjan")
    # TODO: Handle 'response' of type PublicUserObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_users_profile("smedjan")
    # TODO: Handle 'response' of type PublicUserObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PublicUserObject](spotify_web_api/models/public_user_object.py)</code> -- A user

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersProfileErrorBody](spotify_web_api/errors/get_users_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_top_artists(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingArtistObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's top artists based on calculated affinity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_users_top_artists(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopArtistsErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_users_top_artists(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingArtistObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopArtistsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>time_range</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"medium_term"</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingArtistObject](spotify_web_api/models/paging_artist_object.py)</code> -- Pages of artists

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersTopArtistsErrorBody](spotify_web_api/errors/get_users_top_artists_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_users_top_tracks(*, time_range: str | None = "medium_term", limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> PagingTrackObject</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the current user's top tracks based on calculated affinity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_users_top_tracks(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_users_top_tracks(time_range="medium_term", limit=10, offset=5)
    # TODO: Handle 'response' of type PagingTrackObject
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUsersTopTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>time_range</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"medium_term"</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PagingTrackObject](spotify_web_api/models/paging_track_object.py)</code> -- Pages of tracks

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[GetUsersTopTracksErrorBody](spotify_web_api/errors/get_users_top_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unfollow_artists_users(type_: ItemType3OrStr, ids: str, *, body: UnfollowArtistsOrUsersRequest | UnfollowArtistsOrUsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the current user as a follower of one or more artists or other Spotify users.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.unfollow_artists_users(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowArtistsUsersErrorBody
```

**Async**

```python
try:
    await async_client.users.unfollow_artists_users(
        ItemType3.ARTIST, "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowArtistsUsersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[ItemType3OrStr](spotify_web_api/models/enums/item_type3.py)</code> | Value sent with the request. |
| <code>ids</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UnfollowArtistsOrUsersRequest](spotify_web_api/models/unfollow_artists_or_users_request.py) \| [UnfollowArtistsOrUsersRequestDict](spotify_web_api/models/unfollow_artists_or_users_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[UnfollowArtistsUsersErrorBody](spotify_web_api/errors/unfollow_artists_users_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unfollow_playlist(playlist_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the current user as a follower of a playlist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowPlaylistErrorBody
```

**Async**

```python
try:
    await async_client.users.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnfollowPlaylistErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>playlist_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](spotify_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](spotify_web_api/core/exceptions.py)&#91;[UnfollowPlaylistErrorBody](spotify_web_api/errors/unfollow_playlist_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized1](spotify_web_api/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](spotify_web_api/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](spotify_web_api/models/too_many_requests1.py)</code> |
| anything unmapped | <code>[RawError](spotify_web_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

