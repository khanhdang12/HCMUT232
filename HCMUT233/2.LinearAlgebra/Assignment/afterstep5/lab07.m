% Clear the workspace
clear;

% Load user_movies.mat file
load('users_movies.mat', 'movies', 'users_movies', 'users_movies_sort', 'index_small', 'trial_user');

% Get the dimensions
[m, n] = size(users_movies);

% Print a header indicating the movies to be listed
fprintf('Rating is based on the following %d most popular movies:\n', length(index_small));

% Loop through of the popular movies
for j = 1:length(index_small)
    % Print the movie title corresponding to the current index
    fprintf('%d. %s\n', j, movies{index_small(j)});
end

fprintf('\n');

% Select the users to compare to
[m1,n1]=size(users_movies_sort);
ratings=[];
for j=1:m1
    if prod(users_movies_sort(j,:))~=0
        ratings=[ratings; users_movies_sort(j,:)];
    end;
end;

% Find the Euclidean distances
[m2,n2]=size(ratings);
for i=1:m2
    eucl(i)=norm(ratings(i,:)-trial_user);
end;

% Find the smallest Euclidean distances
[smallest_number, position] = min(eucl);
disp(['Smallest Eucl: ', num2str(smallest_number)]);
disp(['Position: ', num2str(position)]);

% Compute the Pearson correlation coefficient
pearson = zeros(size(ratings, 1), 1);
trial_user = trial_user(:)';

% Compute correlation along the ratings vectors
for i=1:size(ratings,1)
    current_rating = ratings(i, :);

    % Compute mean
    trial_user_mean = mean(trial_user);
    current_ratings_mean = mean(current_rating);

    % Subtract with the mean
    trial_user_centered = trial_user - trial_user_mean;
    current_ratings_centered = current_rating - current_ratings_mean;
    
    pearson_numerator = sum(trial_user_centered .* current_ratings_centered);
    pearson_denominator = sqrt(sum(trial_user_centered .^2) .* sum(current_ratings_centered .^2));
    if pearson_denominator ~= 0
        corr = pearson_numerator / pearson_denominator;
    else
        corr = 0;
    end;
    pearson(i) = corr;
end;

% Find the highest Pearson correlation coefficient
[max_pearson, pearson_index] = max(pearson);
disp(['Highest Pearson correlation coefficient: ', num2str(max_pearson)]);
disp(['Position: ', num2str(pearson_index)]);

% Task 9
%% Compare the elements of the vectors DistIndex, PearsonIndex

% Use the position of the smallest Euclidean distance
closest_user_Dist = position;

% Use the index of the highest Pearson correlation coefficient
closest_user_Pearson = pearson_index;

% Compare if the closest user by Euclidean distance is the same as the closest user by Pearson correlation
if closest_user_Dist == closest_user_Pearson
    disp('The closest user based on Euclidean distance is the same as the closest user based on Pearson correlation.');
else
    disp('The closest user based on Euclidean distance is different from the closest user based on Pearson correlation.');
end

% Display the top 5 users for both distance and Pearson correlation for comparison
fprintf('\nTop closest users based on Euclidean distance:\n');
if length(position) >= 5
    disp(position(1:5)');
else
    disp(position');
end

fprintf('Top closest users based on Pearson correlation:\n');
if length(pearson_index) >= 5
    disp(pearson_index(1:5)');
else
    disp(pearson_index');
end

% Task 10
%% Recommendations
% Use the position of the smallest Euclidean distance
closest_user_Dist = position;

% Use the index of the highest Pearson correlation coefficient
closest_user_Pearson = pearson_index;

recommend_dist = [];
for k = 1:n
    if (users_movies(closest_user_Dist, k) == 5)
        recommend_dist = [recommend_dist; k];
    end
end

recommend_Pearson = [];
for k = 1:n
    if (users_movies(closest_user_Pearson, k) == 5)
        recommend_Pearson = [recommend_Pearson; k];
    end
end

liked = [];
for k = 1:20
    if (trial_user(k) == 5)
        liked = [liked; index_small(k)];
    end
end

% Print out the recommendations based on Euclidean distance
fprintf('Recommendations based on Euclidean distance:\n');
for i = 1:length(recommend_dist)
    fprintf('%d. %s\n', i, movies{recommend_dist(i)});
end

% Print out the recommendations based on Pearson correlation
fprintf('\nRecommendations based on Pearson correlation:\n');
for i = 1:length(recommend_Pearson)
    fprintf('%d. %s\n', i, movies{recommend_Pearson(i)});
end

% Print out the movies liked by the trial user
fprintf('\nMovies liked by the trial user:\n');
for i = 1:length(liked)
    fprintf('%d. %s\n', i, movies{liked(i)});
end